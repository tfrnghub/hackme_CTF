# -*- coding: utf-8 -*-
from __future__ import print_function

from abc import ABCMeta, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Manager

from pwn import log
from .config import (DEFAULT_CHARSET,
                     DEFAULT_TOKEN_LENGTH,
                     DEFAULT_HIDDEN_CHAR,
                     DEFAULT_MAX_THREAD,
                     DEFAULT_CHECK_MANUALLY
                     )


class TimeAuthChecker(object):
    __metaclass__ = ABCMeta

    """ Class used to bypass a time based authentication """

    def __init__(self,
                 charset=DEFAULT_CHARSET,
                 token_length=DEFAULT_TOKEN_LENGTH,
                 base_token="",
                 hidden_char=DEFAULT_HIDDEN_CHAR,
                 break_on_time=0,
                 max_thread=DEFAULT_MAX_THREAD,
                 check_manually=DEFAULT_CHECK_MANUALLY):

        """ Checker constructor

        :charset: The charset you need to defined the final token present characters
        :token_length: The length of the result token
        :base_token: If you already found a part of the token, it's not necessary to start from the beguinning
                     if you use this option
        :hidden_char: The character you want to use for the displayed hidden char
        :break_on_time: If you want to stop searching for other offset character when you find a character that took
                        more than break_on_time time unit (in second, can be a float)
        :max_thread: The max count of the threads
        :check_manually: Sometimes you may have to check the result manually, especially when network is horrible
        """
        self._charset = charset
        self._token_length = token_length
        self._hidden_char = hidden_char
        self._break_on_time = break_on_time
        self._token = base_token
        self._max_thread=max_thread
        self._check_manually=check_manually

    @classmethod
    def _avg(cls, l):

        """ Calculate the average of an uniform list

            :l: The list on which you want to calculate the average.
        """

        return sum(l) / float(len(l))

    @abstractmethod
    def request(self, token):
        """
        send the token to server and wait for it return
        :param token: token to send
        :return: time_cost
        """
        pass

    def get_token(self):

        """ Retrieve the string token stored in the object """

        return self._token

    # TODO: break on time
    def process(self):

        """ Iterate on token_length and find more intresting char """
        log.info('Start guessing token ..')
        self._progress = log.progress('Auth ..')
        self._m = Manager()
        self._lock = self._m.Lock()

        offset = 0
        time=0
        while offset < self._token_length:
            cost_time = {}

            with ThreadPoolExecutor(max_workers=self._max_thread) as executor:
                tokens = ['{}{}'.format(self._token, c) for c in self._charset]
                tasks = zip(self._charset, executor.map(self.request_wrap, tokens))

                for c, t in tasks:
                    cost_time[c] = t
                    best_candidate = max(cost_time, key=cost_time.__getitem__)
            
            if cost_time[best_candidate]<time+0.5:
                break
            time=cost_time[best_candidate]
            found_char = best_candidate
            log.success('Finally Flag: {{:{}<{}}}'
                        .format(self._hidden_char, self._token_length)
                        .format(self._token + found_char))

            if self._check_manually:
                log.info('Try again? (Y/N) ')
                if raw_input().upper().strip() == 'Y':
                    continue
            offset += 1
            self._token += found_char

        self._progress.success("DONE! {}".format(self._token))

    def request_wrap(self, token):
        ret=[]
        for i in range(5):
            ret.append(self.request(token))
        ret=min(ret)
        with self._lock:
            print('Current Flag: {{:{}<{}}} {}'
                  .format(self._hidden_char, self._token_length, ret)
                  .format(token))

        return ret

    def print_token(self):

        """ Display the found token """

        log.success("Your token : [{}]".format(self.get_token()))

#!/usr/bin/env python3

import hashlib
import sys

def sha512(s):
    return hashlib.sha512(s.encode()).hexdigest()

def verify(password):
    h = sha512('your hash is ' + sha512(password) + ' but password is not password')

    if h == '2a9b881b84d4386e39518c8802cc8167ec84d37118efd3949dbedd5e73bf74b62d80bf1531b7505a197565660bf452b2641cd5cd12f0c99c502a4d72c28197f2':
        key = bytes.fromhex(sha512('%s really hates her ex.' % password))
        encrypted = bytes.fromhex('20a6b2b83f1731a5bafdc19b4c954cd34419412951e85de45fb904fc5c1a9470eda8d58483e1fb66e3e13f656e0677f75fccb6ff0577e42b5c53620d10178c0f')
        flag = bytearray(i ^ j for i, j in zip(bytearray(key), bytearray(encrypted)))
        print(flag.decode().strip(',.~'))
        return 1
    else:
        #print('Hmmmmm?!')
        return 0
        
#http://aciddr0p.net/pwls.html
# download female-names.txt from http://antirez.com/misc/female-names.txt
f=open("female-names.txt","r")
while True:
    password=f.readline().strip('\n')
    if password=="":
        break
    if verify(password)==1:
        print(password)
        break
f.close()


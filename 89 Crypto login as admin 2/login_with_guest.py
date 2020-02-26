import requests
import base64

url='https://hackme.inndy.tw/login2/'
data={
    "name":"guest",
    "password":"guest"}
r=requests.post(url,data)
for each in r.cookies:
    if each.name=="user":
        user_cookie=each.value

print(base64.b64decode(user_cookie))



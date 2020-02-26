import base64
import re
import json
import binascii
import collections
from gmpy2 import *

from Crypto.Util import number

pattern1=re.compile('RSA\(n=(.*?), e=(.*?)\)')
pattern2=re.compile('Counter\((.*?)\)')

def rsa_encrypt(x):
    v = number.bytes_to_long(x)
    return pow(v, e, n)
    
def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))
    
    
    
def layer4_dec2(data,lenth):
    data=base64.b64decode(data)
    data=xor(data[:-256],data[256:])
    output=b''
    for i in range(0, len(data), 256):
        r=int(binascii.hexlify(data[i:i+256]),16)
        for j in range(0x10000):
            t=rsa_encrypt(('%.4x' % j).encode('latin1'))
            if r==t:
                output=output+binascii.unhexlify('%.4x' % j)
                print(output)
                break
    return output[:lenth]
    
def layer2_3_dec(data):
    d=invert(17,251)
    for key in range(0x100):
        output = []
        for i in data:
            key=(key*0x63+0xf)&0xff
            output.append((i^key)*d%251)
        output=bytes(output)
        if output[4:5]==b'{' and output[-2:]==b'}\n':
            return output

f=open('encrypted','r')
rsa=f.readline().strip('\n')
sha256=f.readline().strip('\n')
counter=f.readline().strip('\n')
enc_data=f.readline().strip('\n')
f.close()

n,e=pattern1.findall(rsa)[0]
n=int(n,16)
e=int(e,16)


counter=pattern2.findall(counter)[0]
counter=json.loads(counter.replace('\'','\"'))


length=0
for char,num in counter.items():
    length=length+num


flag=layer4_dec2(enc_data,length)
print(flag)
flag = layer2_3_dec(flag)
print(flag)







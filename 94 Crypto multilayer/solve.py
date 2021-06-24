import re
import json
import base64
import binascii
from gmpy2 import *
from Crypto.Util import number



patt1_rsa=re.compile("RSA\(n=(.*), e=(.*)\)")
patt2_dic=re.compile('Counter\((.*?)\)')

f=open("encrypted","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
line4=f.readline()

n,e=patt1_rsa.findall(line1)[0]
n=int(n,16)
e=int(e,16)




def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))
def rsa_encrypt(x):
    v = number.bytes_to_long(x)
    return pow(v, e, n)



def compute_length(data):
    raw=patt2_dic.findall(data)[0].replace('\'','\"')
    counter=json.loads(raw)
    length=0
    for char,num in counter.items():
        length=length+num
    return length
def layer4_dec(data):
    xx={}
    for i in range(0x10000):
        r = rsa_encrypt(('%.4x' % i).encode('latin1'))
        block = binascii.unhexlify('%.512x' % r)
        xx[block]=('%.4x' % i)
    data=base64.b64decode(data)
    blocks=xor(data[:-256],data[256:])
    padded=""
    for i in range(0,len(blocks),256):
        padded=padded+xx[blocks[i:i+256]]
    return binascii.unhexlify(padded)
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

length=compute_length(line3)
data=layer4_dec(line4)[:length]
data=layer2_3_dec(data)
print(data)
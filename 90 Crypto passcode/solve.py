from pwn import*
import re
import json


pattern_0=re.compile(b"Try to decode the cipher:\n(.*?)\n====")
pattern_1=re.compile(b"(.*?)\nCalcuate the passcode...")
io = remote('hackme.inndy.tw',7700) 
rec=io.recvuntil("(Press any key to continue)\n")
a=bytes.fromhex(pattern_0.findall(rec)[0].decode())


xx=[]
io.sendline("any key")
io.sendline("any key")
io.sendline("any key")
io.sendline("any key")
io.sendline("any key")
for i in range(0x100):
    io.sendline("any key")
    b=io.recvuntil("(Press any key to continue)\n")    
    xx.append(bytes.fromhex(pattern_1.findall(b)[0].decode()))
io.close()


'''
f=open("enc2","r")
a=bytes.fromhex(f.read())
f.close()

f=open("data2","r")
b=json.load(f)
f.close()
xx=[]
for each in b:
    xx.append(bytes.fromhex(each))
'''


dic={}
for i in range(len(a)):
    dic[i]=[]
    for each in xx:
        if each[i]^a[i] not in dic[i]:
            dic[i].append(each[i]^a[i])

flag=""
for l in range(len(a)):
    for x in range(256):
        aa=[]
        for i in range(97,123):
            aa.append(x^i)
        if sorted(aa)==sorted(dic[l]):
            flag=flag+chr(x)
print(flag)






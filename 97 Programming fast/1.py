from pwn import *
#io=process("./fast")
io=remote('hackme.inndy.tw',7707)
print(io.recvuntil("game.\n"))
io.sendline("Yes I know")
result=[]
for k in range(10000):
    a=io.recvuntil("?\n")
    b=a.split("=")[0]
    if "+" in b:
        b1,b2=b.split("+")
        i1=int(b1)
        i2=int(b2)
        i3=(i1+i2)&0xffffffff
        if i3>0x7fffffff:
            i3=i3-0x100000000 
    elif "/" in b:
        b1,b2=b.split("/")
        i1=int(b1)
        i2=int(b2)
        i3=i1/i2
        if i3<0:
            i3=i3+1
    elif "*" in b:
        b1,b2=b.split("*")
        i1=int(b1)
        i2=int(b2)
        i3=i1*i2
        i3=i3&0xffffffff
        if i3>0x7fffffff:
            i3=i3-0x100000000 
    elif "-" in b:
        if b[0]=='-':
            b1,b2=b[1:].split("-",1)
            i1=-int(b1)
            i2=int(b2)
        else:
            b1,b2=b.split("-",1)
            i1=int(b1)
            i2=int(b2)
        i3=(i1-i2)&0xffffffff
        if i3>0x7fffffff:
            i3=i3-0x100000000 
    result.append(str(i3))
for z in result:
    io.sendline(z)
io.interactive()


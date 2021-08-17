import magic

def cipher(content,password,mode):
    encry=b""
    rnumb=7
    for byte in content:
        for i in range(rnumb&0xff):
            password=(password*0x77+0x39)&0xff
        encry=encry+bytes([byte^password])
        if mode==1:
            rnumb=(21*rnumb//10)^byte
        else:
            z=21*rnumb&0xffffffffffffffff
            rnumb=(z//10)^byte^password
    return encry



f=open("flag.enc","rb")
content=f.read()
f.close()

mode=ord("D")
mode=mode&0xdf
if mode != ord("D"):
	mode = 1
else:
	mode = 0

m = magic.Magic(mime=True)
for password in range(0x100):
    plain=cipher(content,password,mode)
    mime = m.from_buffer(plain)
    if mime != 'application/octet-stream':
        print(password,mime)
        f=open("result-%d"%password,"wb")
        f.write(plain)
        f.close()
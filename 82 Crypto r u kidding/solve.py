
a="EKZF{Hs'r snnn dzrx, itrs bzdrzq bhogdq}"
b="FLAG"


key=1
for i in range(len(b)):
    assert key==(ord(b[i])-ord(a[i]))%26
print("right key")

def decrypt(_in,key):
    result=''
    for i in range(len(_in)):
        ooo=ord(_in[i])
        if ooo>=97 and ooo <=122: 
            ooo=(ooo-97+1)%26+97
            result=result+chr(ooo)
        elif ooo>=65 and ooo <=90: 
            ooo=(ooo-65+1)%26+65
            result=result+chr(ooo)
        else:
            result=result+_in[i]
    return result

print(decrypt(a,key))

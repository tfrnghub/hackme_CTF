
characters = list(''.join(map(chr, range(0x20, 0x7f))))
#print(characters)

dic1={}.fromkeys(characters,0)
dic2={}.fromkeys(characters,0)


f=open("plain.txt","rb")
a=f.read()
f.close()
for i in range(len(a)):
    if chr(a[i])!='\n':
        dic1[chr(a[i])]=dic1[chr(a[i])]+1
#print(dic1)


f=open("crypted.txt","rb")
a=f.read()
f.close()
cry=a

for i in range(len(a)):
    if chr(a[i])!='\n':
        dic2[chr(a[i])]=dic2[chr(a[i])]+1
#print(dic2)


mt={}
for pkey,pvalue in dic1.items():
    if pvalue!=0:
        mt[pkey]=[]
        for ckey,cvalue in dic2.items():
            if pvalue==cvalue:
                mt[pkey].append(ckey)
#print(mt)


intab="".join(mt.keys())
            
tab1=['']
tab2=[]
for key,values in mt.items():
    for value in values:
        for i in range(len(tab1)):
            if value not in tab1[i]:
                tab2.append(tab1[i]+value)
    tab1=tab2
    tab2=[]
i=0


for tab in tab1:
    a=cry.decode()
    dec=a.translate(str.maketrans(tab,intab))
    if 'FLAG{' in dec and 'Well, now they know' in dec and 'Queen' in dec and 'March' in dec and '("Let It Go")' in dec and '[113]' in dec and '@nyw@y}' in dec and 'Dick Zondag' in dec and 'project' in dec and 'Producer' in dec:
        print(dec) 
        i=i+1
#print(i)

        
        
               


    




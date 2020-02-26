import requests
import json

f=open("data","r")
data=json.load(f)
f.close()

for i in range(2):
    r=requests.get("https://hackme.inndy.tw/otp/?issue_otp=1")
    b=r.text.split("\n")
    b.pop()
    data.extend(b)
print(len(data))
f=open("data","w")
json.dump(data,f)
f.close()


data_bin=[]
for each in data:
    data_bin.append(bytes.fromhex(each))
#print(data_bin)


flag=""
for i in range(len(data_bin[0])):
    for j in range(1,0x100):
        for k in range(len(data_bin)):
            if j==data_bin[k][i]:
                break
        if k==len(data)-1:
            #print(i,chr(j))
            flag=flag+chr(j)
print(flag)
if len(flag)!=50:
    print("do it again")
else:
    print("get the right flag")


        

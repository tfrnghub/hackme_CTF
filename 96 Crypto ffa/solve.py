import json
from gmpy2 import *

cry=json.load(open('crypted', 'r'))
M=cry['M']
m=cry['m']
x=cry['x']
y=cry['y']
z=cry['z']
p=cry['p']
q=cry['q']


d=invert(7,m)
c=((x-3*y-z)*d)%m
b=(y+5*c)%m
a=(z-8*c)%m


a_inv=invert(a,M-1)
b_inv=invert(b,M-1)

flag1=pow(p,a_inv,M)
flag1=digits(flag1,16)
print(bytes.fromhex(flag1))

flag2=pow(q,b_inv,M)
flag2=digits(flag2,16)
print(bytes.fromhex(flag2))





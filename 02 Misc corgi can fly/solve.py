from PIL import Image



im = Image.open('corgi-can-fly.png')
source = im.split()
for i in range(3):
	#source[i].show()
	a=source[i].point(lambda i: i%2==1 and 255)
	a.show()


'''
————————————————
# and中含0，返回0； 均为非0时，返回后一个值， 
2 and 0   # 返回0
2 and 1   # 返回1
1 and 2   # 返回2

# or中， 至少有一个非0时，返回第一个非0,
2 or 0   # 返回2
2 or 1   # 返回2
0 or 1   # 返回1 
————————————————
'''

from PIL import Image



im = Image.open('corgi-can-fly.png')
source = im.split()
for i in range(3):
	source[i].show()
	a=source[i].point(lambda i: i%2==1 and 255)
	a.show()



#coding=utf8
from PIL import Image
imbase = Image.open('mandelbrot.gif')
img = imbase.copy()

left = 0.34
top = 0.57+0.027
width = 0.036
height = 0.027
max = 128
diff = []
for j in range(imbase.size[1]):
    for i in range(imbase.size[0]):
        p0 = complex(left+i*width/imbase.size[0],top - (1+j)*height/imbase.size[1])
        p = 0+0j
        for k in range(max):
            p = p**2 + p0
            if p.real**2 + p.imag**2 > 4:
                break
        img.putpixel((i,j),k)
        if k!=imbase.getpixel((i,j)):
            diff.append(k-imbase.getpixel((i,j)))

img.save('out31.png')
imd = Image.new('1',(23,73))
imd.putdata([i<0 for i in diff])
imd.save('out31_2.png')
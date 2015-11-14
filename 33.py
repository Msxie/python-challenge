from PIL import Image
import math

im = Image.open('beer2.png')
data = im.getdata()
color = im.getcolors()
color_len = len(color)
for p in range(65,0,-2):
    dt = []
    value = []
    for i in data:
        if i!=color[p][1] and i!=color[p-1][1]:
            dt.append(i)
            if i!=color[p-2][1]:
                value.append(0)
            else:
                value.append(1)
    data = dt
    n = int(math.sqrt(len(value)))
    newIm = Image.new('1',(n,n))
    newIm.putdata(value)
    newIm.show()

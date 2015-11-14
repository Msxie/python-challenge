#coding=utf8
from PIL import Image
im = Image.open('bell.png')
r,g,b = im.split()
gdata = list(g.getdata())
data = [abs(gdata[i]-gdata[i+1]) for i in range(0,len(gdata),2)]
s = ''
for i in data:
    if i!=42:
        s += chr(i)
print s
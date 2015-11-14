#coding=utf8
from PIL import Image
import string,bz2,keyword
im = Image.open('zigzag.gif')
imdata = im.tostring()
p = im.palette.getdata()[1][::3]
frm = ''.join([chr(i) for i in range(256)])
table = string.maketrans(frm,p)
imdata_tr = imdata.translate(table)

diff = ['','']
newim = Image.new('1',im.size)
for i in range(1,len(imdata)):
    if imdata[i]!=imdata_tr[i-1]:
        diff[0] += imdata[i]
        diff[1] += imdata_tr[i-1]
        newim.putpixel(((i-1)%im.size[0],(i-1)/im.size[0]),1)
newim.save('27.png')
text = bz2.decompress(diff[0])
print text
for i in text.split():
    if not keyword.iskeyword(i):
        print i
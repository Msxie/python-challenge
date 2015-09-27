from PIL import Image

im = Image.open('oxygen.png')
box = (0,43,609,53)
im = im.crop(box)
pixels = im.getdata()
print im.mode
print len(pixels)
print pixels[0]
lim = im.convert('L')
lpixels = lim.getdata()
for i in range(0,609,7):
    print chr(lpixels[i]),

for i in [105,110,116,101,103,114,105,116,121]:
    print chr(i),
from PIL import Image

f = open('yankeedoodle.csv')
l = []
for line in f.readlines():
    l += line.strip()[:-1].split(',')
f.close()

#first
# l = [float(i)*256 for i in l]
# im = Image.new('F',(53,139))
# im.putdata(l)
# im = im.transpose(Image.ROTATE_90)
# im = im.transpose(Image.FLIP_TOP_BOTTOM)
# im.show()
#n = str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]

#second
print ''.join([chr(int(l[i][5] + l[i+1][5] + l[i+2][6])) for i in range(0,len(l)-2,3)])
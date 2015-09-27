from PIL import Image

list = [[i,i-1,i-1,i-2]for i in range(100,1,-2)]
print list
l = len(list)
print l
pos = []
def getpos():
    global pos,list
    for i in range(0,l):
        for p in range(0,list[i][0]):
            pos.append((p+i,i))
        for p in range(0,list[i][1]):
            pos.append((99-i,i+p+1))
        for p in range(0,list[i][2]):
            pos.append((98-p-i,99-i))
        for p in range(0,list[i][3]):
            pos.append((i,98-i-p))
    return pos

getpos()
im = Image.open('wire.png')
print im.mode,im.size
pic = Image.new(im.mode,(100,100))
for k in range(0,10000):
    pic.putpixel(pos[k],im.getpixel((k,0)))

pic.show()
pic.save('14.jpg')


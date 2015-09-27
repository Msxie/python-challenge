from PIL import Image

im = Image.open('mozart.gif')
print im.size,im.mode
image = Image.new(im.mode,(100,100))
def straighten(line):
    for i in range(0,len(line)):
        if line[i]==195:
            break
    return  line[i:] + line[:i]

for i in range(0,im.size[1]):
    line = [im.getpixel((j,i)) for j in range(im.size[0])]
    line = straighten(line)
    for j in range(im.size[0]):
        im.putpixel((j,i),line[j])

im.save('16.gif')

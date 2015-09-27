from PIL import Image

im = Image.open('cave.jpg')
width  = im.size[0]
height = im.size[1]

odd = even = Image.new(im.mode,(width/2,height/2))
for i in range(0,width):
    for j in range(0,height):
        pixel = im.getpixel((i,j))
        if i%2==0 and j%2==0:
            odd.putpixel((i/2,j/2),pixel)
        elif i%2==1 and j%2==1:
            odd.putpixel(((i-1)/2,(j-1)/2),pixel)
        else:
            even.putpixel((i/2,j/2),pixel)

odd.show()
even.show()





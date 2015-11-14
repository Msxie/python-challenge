from PIL import Image,ImageDraw,ImageSequence

white = Image.open('white.gif')
new = Image.new('RGB',white.size,'black')
des = ImageDraw.Draw(new)
x = y = 0
for s in ImageSequence.Iterator(white):
    left, up, right, low = white.getbbox()
    dx = left - 100
    dy = up - 100
    x += dx
    y += dy
    if dx == 0 and dy == 0:
        x += 20
        y += 30
    des.point((x,y))
new.save('22.png')

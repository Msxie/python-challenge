from PIL import Image,ImageDraw

maze = Image.open('maze.png').getdata()
new = Image.new(maze.mode,maze.size,'black')
newImg = ImageDraw.Draw(new)
for i in range(0,maze.size[0]):
    if maze.getpixel((i,0))[0] == 0:
        now = (i,0)
    if maze.getpixel((i,maze.size[0]-1))[0] == 0:
        end = (i,maze.size[0]-1)

wall = (255,)*4
dir = [(1,0),(0,1),(-1,0),(0,-1)]
full_path = []
path = []

while now!=end:
    maze.putpixel(now,wall)
    flag = 0
    nextp = now
    for i in dir:
        try:
            pp = (now[0]+i[0],now[1]+i[1])
            if maze.getpixel(pp)!=wall:
                flag += 1
                nextp = pp
        except:
            pass
    if flag == 0:
        if not path:
            path = full_path.pop()
            continue
        now = path[0]
        path = []
    elif flag > 1:
        full_path.append(path)
        path = [now]
        now = nextp
    else:
        path.append(now)
        now = nextp
else:
    path.append(now)
    full_path.append(path)

for path in full_path:
    for pos in path:
        new.putpixel(pos,wall)

new.save('24.png')

maze = Image.open('maze.png')
data = [maze.getpixel((pos))[0] for path in full_path for pos in path]
f = open('24.zip','wb')
for i in data[1::2]:
    f.write(chr(i))

f.close()



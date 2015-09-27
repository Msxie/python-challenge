f = open('evil.gfx','rb')
content = f.read()
for i in range(5):
    fp = open('12_%d.jpg' % i,'wb')
    fp.write(content[i::5])
    fp.close()
f.close()
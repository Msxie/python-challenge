import urllib,wave
from PIL import Image

for i in range(1,26):
    url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/lake%d.wav' % i
    urllib.urlretrieve(url,'25/lake%d.wav' % i)

slice = []
for i in range(1,26):
    lake = wave.open('25/lake%d.wav' % i,'rb')
    im = Image.new('RGB',(60,60))
    im.frombytes(lake.readframes(lake.getnframes()))
    slice.append(im)
    lake.close()

im = Image.new('RGB',(300,300))
for i in range(0,25):
    im.paste(slice[i],(60*(i%5),60*(i/5)))
im.save('25.jpg')

import urllib,re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
f = urllib.urlopen(url)
row = 0
for line in f.readlines():
    row = row + 1
    if row > 21:
        obj = re.search('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',line)
        if obj:
            print obj.group(1),
f.close()
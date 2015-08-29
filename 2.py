#find alpha in annotation from source code
import urllib,urllib2

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
f = urllib.urlopen(url)
row = 0
for line in f.readlines():
    row = row + 1
    if row > 37:
        for character in line:
            if character.isalpha():
                print character,

f.close()
import urllib,bz2
url = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'
f = urllib.urlopen(url)
l = [chr(len(line)-1) for line in f.readlines()[12::]]
ls = ''.join(l)
print bz2.decompress(ls)
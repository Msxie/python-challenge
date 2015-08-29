import urllib,re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

def create_url(num):
    global url
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num
while True:
    print url
    f = urllib.urlopen(url)
    m = re.search('nothing is (\d+)',f.read())
    if m:
        if m.group(1)== '16044':
            create_url('8022')
        else:
            create_url(m.group(1))
    else:
        break
f.close()

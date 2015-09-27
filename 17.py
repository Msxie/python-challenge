import cookielib
import urllib2,re,urllib
import bz2
import xmlrpclib

#first
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
result = ''

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

def create_url(num):
    global url
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + num

while True:
    print url
    f = urllib.urlopen(url)
    m = re.search('busynothing is (\d+)',f.read())
    f.close()
    opener.open(url)
    for ck in cookie:
        result = result + ck.value
        print ck.name,':',ck.value,'result:',result
    if m:
        create_url(m.group(1))
    else:
        break

#second
result = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
result = urllib.unquote_plus(result)
print bz2.decompress(result)

#third
proxy = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print proxy.phone('Leopold')

#fourth
url2 = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
req = urllib2.Request(url2)
req.add_header('Cookie','info=the flowers are on their way')
resp = opener.open(req)
print resp.read()



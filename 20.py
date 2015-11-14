import re,urllib2,base64
def getResp(start):
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    header = {'Authorization':'Basic '+base64.b64encode('butter:fly'),
              'Range':'bytes=%d-'% start}
    request = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(request)
    print response.info()
    # third
    # nextnum =  re.match('bytes \d+-(\d+)/\d+',response.info()['Content-Range']).group(1)
    # f = open('data.zip','wb')
    # f.write(response.read())
    f.close()
    return int(nextnum)+1

#first
num = 30203
while num < 2123456789:
    print 'num = ',num
    num = getResp(num)

#second
getResp(2123456789)
getResp(2123456743)
msg = 'esrever ni emankcin wen ruoy si drowssap eht'
print msg[::-1]

#third
print getResp(1152983631)

import zipfile,re

z = zipfile.ZipFile('channel.zip','r')
find = re.compile('nothing is (\d+)').search
num = '90052'
while True:
    text = z.read(num+'.txt')
    print z.getinfo(num+'.txt').comment,
#    print text
    match = find(text)
    if not match:
        break
    num = match.group(1)
import hashlib
f = open('mybroken.zip','rb').read()
for i in range(len(f)):
    for j in range(256):
        data = f[0:i] + chr(j) + f[i+1:]
        if hashlib.md5(data).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
            open('mybroken.zip','wb').write(data)
            print i,j
            exit()
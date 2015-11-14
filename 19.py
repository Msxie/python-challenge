import base64,wave

#first
count = 0
india64 = ''
f = open('please!.html')
for line in f.readlines():
    count = count + 1
    if count > 26 and count <1986:
        india64 += line

f.close()
india = base64.decodestring(india64)
open('indian.wav','wb').write(india)

#second
indiai = wave.open('indian.wav','rb')
indiao = wave.open('out.wav','wb')
indiao.setparams(indiai.getparams())
for i in range(indiai.getnframes()):
    indiao.writeframes(indiai.readframes(1)[::-1])
indiai.close()
indiao.close()
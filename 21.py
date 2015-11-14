import zlib,bz2
log = []
data = open('package.pack','rb+').read()
while True:
    if data[0:2] == 'BZ':
        data = bz2.BZ2Decompressor().decompress(data)
        log.append('#')
    elif data[-2:] == 'ZB':
        data = bz2.BZ2Decompressor().decompress(data[::-1])
        log.append('\n')
    elif data[0:2] == 'x\x9c':
        data = zlib.decompress(data)
        log.append(' ')
    elif data[-2:] == '\x9cx':
        data = zlib.decompress(data[::-1])
        log.append('\n')
    else:
        break

print ''.join(log)
print data
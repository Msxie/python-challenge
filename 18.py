import difflib
f = open('delta.txt')
left,right = [],[]
content = f.read().splitlines()
for line in content:
    left.append(line[:53])
    right.append(line[56:])
d = list(difflib.Differ().compare(left,right))

png = ['','','']
for row in d:
    bytes = [chr(int(byte,16)) for byte in row[2:].split()]
    if row[0] == '-':
        png[0] += ''.join(bytes)
    if row[0] == '+':
        png[1] += ''.join(bytes)
    if row[0] == ' ':
        png[2] += ''.join(bytes)

for i in range(3):
    open('18_%d.png' % i,'wb').write(png[i])


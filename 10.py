import re

a = [1, 11, 21, 1211, 111221]
def match_len(par,s):
    return len(re.match(par + '+',s).group())

def gene(s):
    des = ''
    i = 0
    while i < len(s):
        l = match_len(s[i],s[i:])
        des = des + str(l) + s[i]
        i = i + l
    return des

des = '1'
for i in range(1,31):
    des = gene(des)
print len(des)


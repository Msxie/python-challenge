import this
# first  --> i n   t h e   f a c e   o f   w h a t ?
msg = 'va gur snpr bs jung?'
def shift(sh):
    for item in msg:
        if item.isalpha():
            if (ord(item)+sh)> ord('z'):
                new = ord(item)+sh - 122 + 96
            else:
                new = ord(item)+sh
            print chr(new),
        else:
            print item,

for i in range(1,26):
    shift(i)
    print
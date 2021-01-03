a,b = str(input()).split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
a = (''.join(map(str,a)))
b = (''.join(map(str,b)))

if int(a) > int(b) :
    print(int(a))
else :
    print(int(b))
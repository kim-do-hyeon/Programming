a = []
while 1 :
    a = input()
    a = a.split()
    
    if(int(a[0]) == 0 and int(a[1]) == 0):
        break
    else:
        print(int(a[0]) + int(a[1]))
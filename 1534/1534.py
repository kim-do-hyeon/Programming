num = input()
temp = num.split(' ')
value = int(temp[1])
num = int(temp[0])

if (value == 2):
    print(format(num, 'b'))
if (value == 8):
    print(format(num, 'o'))
if (value == 16):
    temp = format(num, 'x')
    temp = temp.upper()
    print(temp)
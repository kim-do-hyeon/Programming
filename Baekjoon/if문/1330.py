a = input()
a = a.split()
num1 = int(a[0])
num2 = int(a[1])

if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
else:
    print("==")
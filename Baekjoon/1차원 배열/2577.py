A = int(input())
B = int(input())
C = int(input())

result = A * B * C

temp = str(result)

for i in range(0,10):
    print(temp.count(str(i)))
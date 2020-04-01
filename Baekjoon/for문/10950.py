num = int(input())

temp1 = []
temp2 = []
result = []
for i in range(num):
    temp = input()
    temp = temp.split()
    add = int(temp[0]) + int(temp[1])
    result.append(add)

for i in range(num):
    print(result[i])
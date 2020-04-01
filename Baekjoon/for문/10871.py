num = input()

num = num.split()
count = int(num[0])
diff = int(num[1])

result = input()
result = result.split()

temp = []
for i in range(count):
    if (int(result[i]) < diff):
        temp.append(result[i])

print(' '.join(temp))
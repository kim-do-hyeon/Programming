a = int(input())

result = []

for i in range(a):
    result.append(list(input().split()))
result.sort(key=lambda x: int(x[0]))

for i in range(a):
    print(result[i][0], result[i][1])
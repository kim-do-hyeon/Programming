num = int(input())
arr = input().split(' ')
count = 0
for j in range(num - 1):
    for i in range(num - 1):
        if (int(arr[i]) > 1000 or int(arr[i]) < -1000):
            print("err")
            
        if int(arr[i]) > int(arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count += 1
            print(arr)
print(count)
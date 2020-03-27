max = 0
arr = [[0 for col in range(5)] for row in range(15)]

for i in range(5):
    arr[i] = input()
    if(len(arr[i]) > max):
        max = len(arr[i])

for i in range(max):
    for j in range(5):
        if (arr[j][i] == None):
            continue
        print(arr[j][i])

#Error
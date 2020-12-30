num = int(input())

for i in range(num) :
    cnt, word = input().split()
    for x in word :
        print(int(cnt) * x, end = '')
    print()
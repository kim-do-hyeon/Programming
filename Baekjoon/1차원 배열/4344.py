import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    list_temp = list(map(int, input().split(' ')))
    average = sum(list_temp[1:]) / list_temp[0]
    count = 0
    for j in list_temp[1:]:
        if j > average:
            count += 1
    print(str('%.3f' % round(count / list_temp[0] * 100, 3)) + '%')
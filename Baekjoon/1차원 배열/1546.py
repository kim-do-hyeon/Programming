N = int(input())
score = list(map(int, input().split()))
temp = 0

modify = []

for i in score:
    modify.append(i/max(score) * 100)

print("%0.2f" % (sum(modify) / N))
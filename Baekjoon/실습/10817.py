import statistics
a = list(input().split())

result = 0
A = int(a[0])
B = int(a[1])
C = int(a[2])

print(statistics.median([A,B,C]))
a = int(input())

for i in range(1, a + 1):
    print(" " * (i - 1) + "*" * (2 * (a - i) + 1))

for j in range(1, a):
    print(" " * (a - j - 1) + "*" * (2 * j + 1))
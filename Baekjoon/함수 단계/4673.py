general = set(range(1, 10001))
change = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    change.add(i)

result = general - change

for i in sorted(result):
    print(i)
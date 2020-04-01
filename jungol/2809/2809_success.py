n = int(input())
for i in range(int(1)):
    d = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            d.append(i)
            if i!=n//i:
                d.append(n//i)
sort = d.sort()
print(" ".join(map(str, d)))

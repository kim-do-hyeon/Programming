dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
temp = str(input())

count = 0

for i in range(len(temp)) :
    for j in dial :
        if temp[i] in j :
            count += dial.index(j) + 3
print(count)
N = int(input())

for i in range(N):
    score = 0
    cnt = 0
    result = input()
    for j in range(len(result)):
        if result[j] == 'O':
            cnt += 1
            score += cnt
        elif result[j] == 'X':
                score += 0
                cnt = 0
    print(score)
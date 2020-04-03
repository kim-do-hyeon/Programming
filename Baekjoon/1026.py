N = int(input())
if (N > 50):
    print("Error")

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B)

result = 0

for i in range(N):
    result += A[i] * B[i]

print(result)
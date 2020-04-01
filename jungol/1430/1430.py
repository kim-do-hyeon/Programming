A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_list = list(str(result))
for i in range(10):
    result_num_list = result_list.count(str(i))
    print(result_num_list)
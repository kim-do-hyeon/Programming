num_list = []

for i in range(9):
    temp = int(input())
    num_list.append(temp)
max_result = max(num_list)
print(max_result)
print(num_list.index(max_result) + 1)
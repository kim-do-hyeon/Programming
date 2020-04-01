a = input()
result = list(a)
list_count = len(result)
height = 10
for i in range (1, list_count):
    if (result[i] == result[i - 1]):
        height += 5
    elif (result[i] != result[i - 1]):
        height += 10
    else:
        print("Err")
print(height)
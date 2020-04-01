num = input()
temp = num.split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])
result_a = (a+b)%c
result_b = ((a%c)+(b%c))%c
result_c = (a*b)%c
result_d = ((a%c)*(b%c))%c

print(result_a)
print(result_b)
print(result_c)
print(result_d)
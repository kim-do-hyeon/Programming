for i in range(3):
    n = int(input())
    if i:
        if min_temp > n:
            min_temp = n
    else :
        min_temp = n

for i in range(2):
    n = int(input())
    if i:
        if beverage_temp > n:
            beverage_temp = n
    else:
        beverage_temp = n
print(min_temp + beverage_temp - 50)
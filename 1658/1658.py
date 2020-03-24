from math import gcd
def lcm(x,y):
    return x * y // gcd(x,y)

a = input()
temp = a.split(' ')
print(gcd(int(temp[0]), int(temp[1])))
print(lcm(int(temp[0]), int(temp[1])))
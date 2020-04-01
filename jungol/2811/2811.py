num = input()
result = num.split(' ')

def prime_number(n):
    if (int(n) < 2):
        return False
    for i in range(2, int(n)):
        if (int(n) % i == 0):
            return 0
    return 1
    

for i in range(5):
    if int(result[i]) < 2:
        print("number one")
    elif(prime_number(result[i])):
        print("prime number")
    else:
        print("composite number")
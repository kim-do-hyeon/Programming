a = float(input())

if (a <= 50.80):
    print("Flyweight")
elif (a > 50.80 and a <= 61.23):
    print("Lightweight")
elif (a > 61.23 and a <= 72.57):
    print("Middleweight")
elif (a > 72.57 and a <= 88.45):
    print("Cruiserweight")
else:
    print("Heavyweight")
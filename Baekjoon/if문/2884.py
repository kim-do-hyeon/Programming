a = input()
a = a.split()

hour = int(a[0])
minute = int(a[1])

if (minute - 45 < 0) :
    hour = hour - 1
    if(hour < 0):
        hour = 23
    minute = minute + 15
    print(hour, minute)
else:
    minute = minute - 45
    print(hour, minute)
sthour, stmin = input().split()

hour = int(sthour)
min = int(stmin)

if(min < 45):
    if(hour == 0):
        hour = 23
        min = 60 - (45 - min)
    else:
        hour -= 1
        min = 60 - (45 - min)
else:
    min -= 45

print(hour, min)
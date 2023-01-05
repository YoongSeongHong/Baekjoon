import sys

n = int(sys.stdin.readline())
price = 1000 - n
count = 0
while price > 0:
    if price % 500 == 0:
        count += price // 500
        break
    elif price // 500 != 0:
        count += price // 500
        price = price % 500
    elif price % 100 == 0:
        count += price // 100
        break
    elif price // 100 != 0:
        count += price // 100
        price = price % 100
    elif price % 50 == 0:
        count += price // 50
        break
    elif price // 50 != 0:
        count += price // 50
        price = price % 50
    elif price % 10 == 0:
        count += price // 10
        break
    elif price // 10 != 0:
        count += price // 10
        price = price % 10
    elif price % 5 == 0:
        count += price // 5
        break
    elif price // 5 != 0:
        count += price // 5
        price = price % 5
    else:
        count += price
        break

print(count)
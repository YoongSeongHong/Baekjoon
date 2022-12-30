import sys

arr = []
while(True):
    try:
        a, b = map(int, sys.stdin.readline().split())
        arr.append(a+b)

    except:
        for i in range(len(arr)):
            print(arr[i])
        sys.exit()
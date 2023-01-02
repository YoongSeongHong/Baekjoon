import sys

arr = []
while(True):
    a, b = map(int, sys.stdin.readline().split())
    if(a == 0 and b == 0):
        break
    arr.append(a+b)

for i in range(len(arr)):
    print(arr[i])
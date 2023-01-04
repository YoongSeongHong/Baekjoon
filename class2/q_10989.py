import sys

T = int(sys.stdin.readline())
arr = [0]*10001

for i in range(T):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    if(arr[i] != 0):
        for j in range(arr[i]):
            print(i)
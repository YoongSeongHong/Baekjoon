import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = list(sys.stdin.readline().split())
    arr.append(a)
    arr[i][0] = int(arr[i][0])

arr = sorted(arr, key=lambda arr: arr[0])
for i in range(n):
    print(arr[i][0], arr[i][1])
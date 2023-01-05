import sys

N = int(sys.stdin.readline())
arr = [[0 for j in range(2)] for i in range(N)]
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr[i][0] = x
    arr[i][1] = y
arr = sorted(arr, key=lambda arr: arr[1])
arr = sorted(arr, key=lambda arr: arr[0])

for i in range(N):
    print(arr[i][0], arr[i][1])

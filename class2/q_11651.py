import sys

n = int(sys.stdin.readline())
arr = [[0 for col in range(2)] for row in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = map(int, sys.stdin.readline().split())

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

for i in range(n):
    print(arr[i][0], arr[i][1])
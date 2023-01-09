import sys

N = int(sys.stdin.readline())
arr = []
result = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)
for i in range(N):
    bigger = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            bigger += 1
    result.append(bigger)
for i in range(N):
    print(result[i]+1, end=' ')
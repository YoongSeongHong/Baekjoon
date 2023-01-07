import sys

N, K = map(int, sys.stdin.readline().split())
arr = [0] * N
stack = []
for i in range(N):
    arr[i] = i+1

while len(arr) != 0:
    if len(arr) >= K:
        stack.append(arr.pop(K-1))
        for i in range(K-1):
            arr.append(arr.pop(0))
    else:
        n = K % len(arr)
        stack.append(arr.pop(n-1))
        if n != 1:
            for i in range(n-1):
                arr.append(arr.pop(0))
print('<', end='')
for i in stack:
    if i != stack[-1]:
        print(i, end=', ')
    else:
        print(i, end='')
print('>')
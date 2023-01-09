import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
arr = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            s = cards[i] + cards[j] + cards[k]
            arr.append(s)
arr.sort()
result = 0
for i in range(len(arr)):
    if arr[i] <= M:
        result = arr[i]
    else:
        break
print(result)
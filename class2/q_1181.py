import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    word = sys.stdin.readline().rstrip()
    arr.append(word)
s = set(arr)
arr = list(s)
arr.sort()
arr.sort(key=lambda x : len(x))
for i in range(len(arr)):
    print(arr[i])
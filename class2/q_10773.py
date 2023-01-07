import sys
from collections import deque

K = int(sys.stdin.readline())
lst = deque()
s = 0
for i in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        lst.pop()
    else:
        lst.append(n)
s = sum(lst)
print(s)
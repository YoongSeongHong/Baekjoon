# 11399번 ATM
import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
# 합의 최솟값이 나오기 위해서는 정렬 순으로 더해야 함
P.sort()
lst = []
s = 0
for i in range(N):
    s += P[i]
    lst.append(s)
print(sum(lst))
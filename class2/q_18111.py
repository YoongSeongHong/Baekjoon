#18111번 마인크래프트
import sys

N, M, B = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)

for i in range(N):
    print(lst[i])

print(max(lst))
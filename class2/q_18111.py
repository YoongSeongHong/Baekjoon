#18111번 마인크래프트
import sys

N, M, B = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst = lst + a

mx = max(lst)
mn = min(lst)

for i in range(mn, mx+1):
    block = B
    for j in range(len(lst)):



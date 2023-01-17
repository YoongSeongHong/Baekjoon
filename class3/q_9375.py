# 9375번 패션왕 신해빈
import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    dic = {}
    com = 1
    for j in range(n):
        key, value = sys.stdin.readline().split()
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
    for v in dic.values():
        com *= (v+1)
    print(com - 1)

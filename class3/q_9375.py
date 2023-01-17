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
            # 키에 옷 종류, 값에 종류 수 저장
            dic[value] += 1
        else:
            dic[value] = 1
    for v in dic.values():
        # v+1Cv = v+1. 예를 들어 종류가 3 3 2면 4 * 4 * 3 - 1
        com *= (v+1)
    print(com - 1)

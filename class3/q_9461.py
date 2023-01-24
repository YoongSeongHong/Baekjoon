# 9461번 파도반 수열
import sys

T = int(sys.stdin.readline())
p = [0] * 101
for i in range(T):
    # dp 이용
    p[1] = 1
    p[2] = 1
    p[3] = 1
    n = int(sys.stdin.readline())
    for j in range(4, n+1):  # 점화식은 간단하다.
        if p[j] == 0:
            p[j] = p[j-2] + p[j-3]
    print(p[n])

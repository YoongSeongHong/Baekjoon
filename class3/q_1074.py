# 1074번 Z
import sys


def solution(x, y, N):
    global cnt
    l = N // 2
    for i in range(x, x+N):
        for j in range(y, y+N):
            if j == c and i == r:
                return

            arr[i][j] = cnt
            solution(x, y, l)
            solution(x, y+l, l)
            solution(x+l, y, l)
            solution(x+l, y+l, l)
            cnt += 1
            return


N, r, c = map(int, sys.stdin.readline().split())
arr = [[0 for j in range(2**N)] for i in range(2**N)]
visit = []
cnt = 0
solution(0, 0, 2**N)
for i in range(2**N):
    print(arr[i])

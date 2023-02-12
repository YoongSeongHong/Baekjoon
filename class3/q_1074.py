# 1074번 Z
import sys


def solution(x, y, N):
    global cnt
    # 분할 했을때 그 구역에 r, c가 없으면 N*N을 cnt에 더해준다
    if x > r or x + N <= r or y > c or y + N <= c:
        cnt += N ** 2
        return

    # 분할 된 구역에 r,c가 존재하면 그 안에서만 재귀로 r,c 찾아주면 됨
    if N > 2:
        l = N // 2
        solution(x, y, l)
        solution(x, y+l, l)
        solution(x+l, y, l)
        solution(x+l, y+l, l)
    else:  # N이 1일때 : 네 가지 중에 하나.
        if x == r and y == c:  # z의 1번 위치
            print(cnt)
        elif x == r and y + 1 == c:  # z의 2번 위치
            print(cnt + 1)
        elif x + 1 == r and y == c:  # z의 3번 위치
            print(cnt + 2)
        else:  # z의 4번 위치
            print(cnt + 3)
        sys.exit()  # cnt 출력하고 종료


N, r, c = map(int, sys.stdin.readline().split())
cnt = 0
solution(0, 0, 2**N)

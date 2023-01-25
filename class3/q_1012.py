# 1012번 유기농 배추
import sys
from collections import deque

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def bfs(lst, a, b):  # deque 사용한 bfs
    dq = deque()
    dq.append((a, b))
    lst[a][b] = 0  # 검사 한 노드는 0으로
    while dq:
        x, y = dq.popleft()
        for i in range(4):  # 노드를 기준으로 위, 왼쪽, 오른쪽, 아래 순으로 검사
            rx = x + dx[i]
            ry = y + dy[i]
            if rx < 0 or rx >= N or ry < 0 or ry >= M:  # 인덱스 벗어나는 경우
                continue
            if lst[rx][ry] == 1:  # 검사 하면서 1 나온 인덱스 데크에 추가
                dq.append((rx, ry))
                lst[rx][ry] = 0


T = int(sys.stdin.readline())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    lst = [[0] * M for _ in range(N)]  # 가로 M, 세로 N인 이차원 배열 생성, 초깃값 모두 0
    count = 0  # 필요한 지렁이 수
    for j in range(K):  # 배추 있는 자리는 1
        r, c = map(int, sys.stdin.readline().split())
        lst[c][r] = 1

    for k in range(N):  # 인덱스 차례 대로 검사.
        for l in range(M):
            if lst[k][l] == 1:
                bfs(lst, k, l)  # bfs 한 번 돌면 한 지역 검사 끝
                count += 1
    print(count)





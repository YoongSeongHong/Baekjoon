# 7576번 토마토
import sys
from collections import deque

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def bfs(graph):
    dq = deque()
    # 루트는 각각 익은 토마토 들로부터 시작함
    for t in range(len(arr)):
        dq.append(arr[t])

    while dq:  # deque에 남아 있는 동안 반복
        y, x = dq.popleft()
        for k in range(4):
            # 4번 돌리면서 자동으로 위, 왼쪽, 오른쪽, 아래 검사
            mx = x + dx[k]
            my = y + dy[k]
            # 틀 벗어 나면 continue
            if mx >= M or mx < 0 or my >= N or my < 0:
                continue
            if graph[my][mx] == 0:
                dq.append((my, mx))
                graph[my][mx] = graph[y][x] + 1


M, N = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

check = 0
arr = []
result = 0
# 1인 인덱스들을 먼저 따로 저장
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            arr.append((i, j))
        elif graph[i][j] == 0:
            check = 1  # 맨처음 토마토 밭에 안익은 토마토가 없으면 check를 1로 바꿔서 0 출력하게함

if check == 0:
    print(0)
elif check == 1:
    bfs(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)  # 결과 토마토밭에 안 익은 토마토가 있으면 -1 출력하고 종료
                sys.exit()
            result = max(result, graph[i][j] - 1)  # 각 인덱스는 직전 인덱스의 값 + 1 저장하는데 1부터 시작하므로 1 빼줘야함
    print(result)




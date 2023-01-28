# 10026번 적록색약
import sys
import copy
from collections import deque

# bfs에서 for문 돌릴 때 위, 왼쪽, 오른쪽, 아래 순서 대로 검사 하기 위함
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


# 적록 색약 아닌 사람의 구역 수
def bfs_n(graph, a, b, color):  # 그래프, i, j, 색깔을 매개 변수로 받음
    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0  # 검사 마친 구역은 0으로
    while dq:
        x, y = dq.popleft()
        for i in range(4):  # 위, 왼쪽, 오른쪽, 아래 순서 대로 검사
            mx = x + dx[i]
            my = y + dy[i]
            # 인덱스가 구역 벗어 나면 continue로 다음 구역 검사
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            if graph[mx][my] == color:  # 다음 인덱스의 색깔이 현재와 같으면 append
                dq.append((mx, my))
                graph[mx][my] = 0  # 검사 마친 인덱스는 0으로


# 적록 색약의 구역 수
def bfs_a(graph, a, b, color):  # 그래프, i, j, 색깔을 매개 변수로 받음
    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0  # 검사 마친 구역은 0으로
    while dq:
        x, y = dq.popleft()
        for i in range(4):  # 위, 왼쪽, 오른쪽, 아래 순서 대로 검사
            mx = x + dx[i]
            my = y + dy[i]
            # 인덱스가 구역 벗어 나면 continue로 다음 구역 검사
            if mx < 0 or mx >= N or my < 0 or my >= N:
                continue
            # 현재 인덱스 색깔이 R이나 G이고, 다음 인덱스가 R이나 G이면 같은 색으로 봄.
            if (color == 'R' or color == 'G') and (graph[mx][my] == 'R' or graph[mx][my] == 'G'):
                dq.append((mx, my))
                graph[mx][my] = 0
            # 파랑은 파랑 끼리만 같은 색으로 봄
            elif color == 'B' and graph[mx][my] == 'B':
                dq.append((mx, my))
                graph[mx][my] = 0


N = int(sys.stdin.readline())
graph = []
for i in range(N):
    s = list(sys.stdin.readline().rstrip())  # 한 행을 리스트로 그 안에 한 글자씩 저장
    graph.append(s)
graph2 = copy.deepcopy(graph)  # graph와 생김새만 같은 다른 객체 복사

normal_count = 0  # 적록 색약 아닌 사람이 보는 구역 수
blind_count = 0  # 적록 색약인 사람이 보는 구역 수
# 적록 색약이 아닌 사람 부터 검사 시작
for i in range(N):  # 행
    for j in range(N):  # 열
        if graph[i][j] == 0:  # 0이면 이미 검사 끝난 인덱스임
            continue
        else:
            # bfs_n 한번 돌고 나면 한 구역 검사 완료
            bfs_n(graph, i, j, graph[i][j])
            normal_count += 1

# 적록 색약인 사람 검사 시작. for문 자체는 위와 같다.
for i in range(N):
    for j in range(N):
        if graph2[i][j] == 0:
            continue
        else:
            bfs_a(graph2, i, j, graph2[i][j])
            blind_count += 1

print(normal_count, blind_count)
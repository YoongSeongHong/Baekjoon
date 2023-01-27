# 1388번 바닥 장식
import sys
from collections import deque


# 연속된 '-' 검사할 때 쓸 함수
def bfs_x(graph, a, b): # a = y, b = x
    dq = deque()
    dq.append(b)  # 검사 시작 하는 graph[i][j]가 루트
    graph[a][b] = 0  # 방문한 노드는 0으로 바꿔 줘야 한다.
    while dq:  # 데크에 값 남은 동안 반복
        x = dq.popleft()
        if x+1 >= M:  # ex) 1행을 검사 할 때 가로 길이 넘어 가면 break. 어차피 같은 행 인덱스에서만 이어짐.
            break
        if graph[a][x+1] == '-':  # 검사 하는 인덱스의 다음 값도 '-'이면
            dq.append(x+1)  # dq에 append 하여 while문 지속
            graph[a][x+1] = 0  # 검사 할 노드 미리 0으로 바꿔줌


# 연속된 '|' 검사할 때 쓸 함수
def bfs_y(graph, a, b):  # a = y, b = x
    dq = deque()
    dq.append(a)  # 검사 시작 하는 graph[i][j]가 루트
    graph[a][b] = 0  # 방문한 노드는 0으로 바꿔 줘야 한다.
    while dq:  # 데크에 값 남은 동안 반복
        y = dq.popleft()
        if y+1 >= N:  # ex) 1열을 검사 할 때 세로 길이 넘어 가면 break. 어차피 같은 열 인덱스에서만 이어짐.
            break
        if graph[y+1][b] == '|':  # 작대기 다른거 쓰면 피본다... 검사 하는 인덱스의 다음 값도 '|'이면
            dq.append(y+1)  # dq에 append 하여 while문 지속
            graph[y+1][b] = 0  # 검사 할 노드 미리 0으로 바꿔줌


N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):  # 이차원 배열로 저장 행/열
    s = list(sys.stdin.readline().rstrip())
    graph.append(s)

count = 0  # 장식 수를 카운트 할 변수
for i in range(N):
    for j in range(M):  # 1행부터 검사
        if graph[i][j] == '-':  # 검사 하다가 만난 문자가 '-' 이면 -에 대한 bfs
            bfs_x(graph, i, j)  # bfs 함수 한 번 돌면 연속된 '-' 를 하나 끝냄
            count += 1  # 하나 끝내면 카운트 + 1
        elif graph[i][j] == '|':  # 검사 하다가 만난 문자가 '|' 이면 |에 대한 bfs
            bfs_y(graph, i, j)  # bfs 함수 한 번 돌면 연속된 '|' 를 하나 끝냄
            count += 1 # 하나 끝내면 카운트 + 1

print(count)

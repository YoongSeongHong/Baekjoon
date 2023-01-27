# 2606번  바이러스
import sys
from collections import deque


def bfs(graph):  # 너비 우선 탐색 이용, deque
    dq = deque()
    dq.append(1)  # 문제에서 루트는 1이라고 주어져 있다.
    visited = []  # 방문한 노드 값을 저장할 리스트
    while dq:  # 데크에 값이 안남을 때 까지 탐색을 하면 루트 1과 연결된 모든 노드 검사한 것
        n = dq.popleft() # 너비 우선 탐색이므로 가장 밑에 있는 값부터 pop
        if n not in visited: # 방문한 노드는 visited에 추가
            visited.append(n)
        if n in graph:
            dq += list(set(graph[n]) - set(visited))  # n과 인접한 노드 중 이미 탐색한 노드를 빼고 append한다.

    return len(visited) - 1  # 루트 1에서 부터 방문할 수 있는 노드 수 중 1을 뺀 크기


n = int(sys.stdin.readline())
link = int(sys.stdin.readline())
graph = {}  # 링크가 있는 노드를 키로 저장 하고, 각 엣지를 값으로 저장
for i in range(link):
    start, end = map(int, sys.stdin.readline().split())
    if start not in graph:  # graph에 없었으면 배열을 값으로 갖는 키 생성, 엣지 저장
        graph[start] = []
        graph[start].append(end)
    else:
        graph[start].append(end)
    if end not in graph:
        graph[end] = []
        graph[end].append(start)
    else:
        graph[end].append(start)
print(bfs(graph))

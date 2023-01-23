# 1260번 DFS와 BFS
import sys
from collections import deque


def DFS(graph, root):  # DFS 는 스택 이용
    visited = []
    stack = [root]  # 루트 부터 시작
    while stack:  # 스택에 값이 안 남을 때까지 반복
        n = stack.pop()
        if n not in visited:
            visited.append(n)  # visited 에 없는 n 집어 넣고
            if n in graph:  # n 간선 존재 한다면
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)  # 역 정렬 해서 stack 에 더해 주어야 pop 은 작은 값부터 나온다.
                stack += temp

    return " ".join(str(i) for i in visited)


def BFS(graph, root):  # BFS 는 deque 이용
    visited = []
    dq = deque()
    dq.append(root)  # 루트 부터 시작
    while dq:  # 데크에 값이 안 남을 때 까지 반복
        n = dq.popleft()  # 맨 앞 값을 pop 하고
        if n not in visited:
            visited.append(n)  # visited 에 없는 값이면 append 한다.
            if n in graph:
                temp = graph[n]  # n 인접 노드 저장
                temp.sort()  # 큐 이므로 오름 차순 정렬 해야 작은 값 부터 pop 한다.
                dq += graph[n]
    return " ".join(str(i) for i in visited)


N, M, V = map(int, sys.stdin.readline().split())
graph = {}  # 각 숫자를 키, 인접 노드를 값으로 가지는 딕셔너리 생성
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start not in graph:  # 그래프 딕셔너리 없는 키이면
        graph[start] = []  # 키, 값 모두 추가. 값은 리스트 형식 으로 저장 한다.
        graph[start].append(end)
    else:
        graph[start].append(end)  # 이미 있는 키이면 값 리스트에 append
    if end not in graph:  # 도착 엣지도 마찬 가지
        graph[end] = []
        graph[end].append(start)
    else:
        graph[end].append(start)

print(DFS(graph, V))
print(BFS(graph, V))
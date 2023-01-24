# 11724번 연결 요소의 개수
import sys

N, M = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for i in range(M):  # graph 딕셔너리에 엣지들을 키로 갖고 각각 인접 노드 배열을 값으로 갖는다.
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

result = 0
visited = []
while len(visited) < N:  # 모든 노드가 방문 되면 종료
    stack = [min(graph.keys())]  # DFS, 스택 이용
    while stack:  # while 문 한 번은 연결 요소 하나.
        n = stack.pop()  # 스택 가장 위엣 값 pop
        if n not in visited:  # 그 값이 처음 방문 되었다면
            visited.append(n)  # visited 에 추가
            if n in graph:
                temp = graph[n]
                temp.sort(reverse=True)  # stack 은 내림차순으로 추가해야 pop할 때 오름차순으로 나온다.
                stack += temp
    for k in visited:  # 이미 검사한 연결 요소의 값들은 그래프에서 제거
        if k in graph:
            graph.pop(k)
    result += 1  # 연결 요소 수 추가
print(result)





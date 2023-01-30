# 1697번 숨바꼭질
import sys
from collections import deque


# bfs로 해결
def bfs(graph, root, dest):  # 그래프, 루트, K값을 매개변수로
    dq = deque()
    dq.append(root)
    while dq:
        n = dq.popleft()
        if n == dest:
            return graph[dest]  # 그래프의 인덱스는 각각 최소 경로 수 저장
        for i in (n-1, n+1, n*2):
            if i >= 0 and i <= 100000 and graph[i] == 0:  # 최단 값을 인덱스에 저장.
                graph[i] = graph[n] + 1
                dq.append(i)


N, K = map(int, sys.stdin.readline().split())
graph = [0] * 100001
print(bfs(graph, N, K))


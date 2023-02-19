# 1446번 지름길
import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    q = []  # q에는 도착지점과 그 최소비용 저장
    heapq.heappush(q, (0, start))  # 처음엔 시작점과 0 저장
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # distance[now] 에 최솟값이 저장되었는지 확인
        if distance[now] < dist:  # 예제 1에서 (50, 10) 넣은 후이므로 (50, 20)은 무시하는 것
            continue
        for i in graph[now]:
            # cost는 곧 다음 지점의 dist가 된다.
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 여러 경로 중 최솟값 저장
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range((d+1))]
# 거리 일단 무한대로 초기화
distance = [INF] * (d+1)

# 그래프 i번째는 시작점 의미, 튜플 값은 각각 도착점, 거리 의미
for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    # 도착지가 d보다 크면 의미 없으므로 저장 x
    if b > d:
        continue
    # 지름길의 출발점, 도착점, 거리 입력받아서 그래프의 출발점의 인덱스에  도착점, 거리 저장
    graph[a].append((b, c))

dijkstra(0)
print(distance[d])

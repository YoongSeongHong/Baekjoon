# 13549번 숨바꼭질 3
import sys
import heapq


# 지름길 문제와 거의 동일
def dijkstra(start):
    q = []  # q에 도착지점과 그 시간 저장
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작 지점에서 시작 지점까지 걸리는 시간은 0
    while q:
        # now는 현재 검사하는 노드, dist는 그 노드까지의 최소시간 저장
        dist, now = heapq.heappop(q)
        # distance[now]가 dist보다 작다는건 이미 최소시간을 distance가 저장하고 있다는 의미 -> 검사 안해도 됨
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # cost는 현재 노드까지의 시간 + 현재 노드에서 다음 노드까지의 시간 = 시작부터 다음 노드까지의 시간
            cost = dist + i[1]
            # 그 cost가 distance[i[0]]보다 작으면 최신화
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # q에 다음 노드 내용 저장
                heapq.heappush(q, (cost, i[0]))


n, k = map(int, sys.stdin.readline().split())
size = max(n, k)
INF = int(1e9)  # 무한대 의미
graph = [[] for _ in range(((size*2)+1))]  # k보다 더 넉넉하게 사이즈 잡아주자. 줄여도 되긴할듯
distance = [INF] * ((size*2)+1)  # 그 노드까지 최소거리 저장할 리스트
for i in range((size*2)+1):
    # 각각 인덱스 에러 안나게 범위 조건 추가해서 graph[i][0]엔 다음노드, graph[i][1]엔 그 노드까지 걸리는 시간 저장
    if i+1 <= size*2:
        graph[i].append((i+1, 1))
    if i-1 >= 0:
        graph[i].append((i-1, 1))
    if i*2 <= size*2:
        graph[i].append((i*2, 0))

dijkstra(n)
print(distance[k])

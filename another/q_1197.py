# 1197번 최소 스패닝 트리
import sys


# 부모를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:  # x가 루트가 아니라면 (부모가 있다면)
        parent[x] = find_parent(parent, parent[x])  # 재귀 이용
    return parent[x]


# 루트를 같게 만드는(같은 집합에 넣는) 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)  # a의 루트
    b = find_parent(parent, b)  # b의 루트
    if a < b:  # a 루트가 b 루트보다 작으면 a가 b의 부모가 된다.
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
edge = []  # 간선 저장할 리스트
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((a, b, c))
edge.sort(key=lambda x: x[2])  # 비용 기준으로 오름차순 정렬

parent = [0] * (v+1)  # 각 인덱스 값은 그 부모 노드를 가리킴
for i in range(1, v+1):
    parent[i] = i  # 처음엔 자기 자신으로 초기화

cost_sum = 0  # 총 비용 저장할 변수

for i in edge:
    a, b, cost = i
    # a, b의 루트가 다르다면(다른 집합에 있다면) -> 아직 간선 연결 안 된 것
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)  # 최소 비용으로 둘을 이어줌
        cost_sum += cost

print(cost_sum)

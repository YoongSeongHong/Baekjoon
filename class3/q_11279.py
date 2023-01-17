# 11279번 최대 힙
import sys
import heapq
# 최대 힙 -> 최소 힙에서 -만 붙여 주기

N = int(sys.stdin.readline())
hq = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        # 최대 힙 사용 하면 힙 구조 유지 하면서 인덱스 0에 최솟값 저장
        heapq.heappush(hq, -n)
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))

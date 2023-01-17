# 1927번 최소 힙
import sys
from queue import PriorityQueue
# 우선 순위 큐 이용.

N = int(sys.stdin.readline())
que = PriorityQueue()
for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        # 우선 순위 큐는 자동 으로 정렬 해줌
        que.put(n)
    else:
        if que.qsize() == 0:
            print(0)
        else:
            print(que.get())

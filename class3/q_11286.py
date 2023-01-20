# 11286번 절댓값 힙
import sys
import heapq

N = int(sys.stdin.readline())
hq = []
# 딕셔너리에 절댓값을 키, 음수의 수를 값을 저장하는 방식 이용
dic = {}
for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        # n이 음수 이면 절댓값 키에 +1 하고, 나중에 키에 존재 하는 + 수 만큼 -를 대신 출력
        if n < 0:
            # 힙 큐에 저장은 절댓값 으로 저장
            heapq.heappush(hq, -n)
            if -n not in dic:
                dic[-n] = 1
            else:
                dic[-n] += 1
        else:
            heapq.heappush(hq, n)
    else:
        # 비어 있으면 0 출력
        if len(hq) == 0:
            print(0)
        else:
            # 음수가 들어 왔던 만큼 -를 씌워 출력 한다.
            if hq[0] in dic and dic[hq[0]] > 0:
                dic[hq[0]] -= 1
                print(-heapq.heappop(hq))

            else:
                print(heapq.heappop(hq))

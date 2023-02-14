# 7662번 이중 우선순위 큐
import sys
import heapq

T = int(sys.stdin.readline())

for i in range(T):
    heap_max = []  # 최댓값을 반환할 때 이용
    heap_min = []  # 최솟값을 반환할 때 이용
    k = int(sys.stdin.readline())
    visited = [False] * k  # 남아있는 값이면 True로 저장. max나 min중 하나에서라도 pop되면 False 저장
    for j in range(k):
        order, num = map(str, sys.stdin.readline().split())
        if order == 'I':  #
            heapq.heappush(heap_max, (-int(num), j))  # 최대 힙에 저장
            heapq.heappush(heap_min, (int(num), j))  # 최소 힙에 저장
            visited[j] = True
        else:
            if num == '1':
                # 최대 힙에 값이 존재하고 최소 힙과 공유하는 visited의 인덱스 값이 False면 최소 힙에서 pop했다는 의미
                while heap_max and visited[heap_max[0][1]] == False:
                    heapq.heappop(heap_max)  # 최대 힙에서도 그 값 빼준다.
                if heap_max:  # 최대 힙에 값 존재할 때
                    visited[heap_max[0][1]] = False  # 최소 힙과 공유하는 visited의 인덱스 False로 바꿔줌
                    heapq.heappop(heap_max)  # 최대 힙에서 값 뺌
            else:
                # 최소 힙에 값이 존재하고 최대 힙과 공유하는 visited의 인덱스 값이 False면 최대 힙에서 pop했다는 의미
                while heap_min and visited[heap_min[0][1]] == False:
                    heapq.heappop(heap_min)  # 최소 힙에서도 그 값 빼준다.
                if heap_min:  # 최소 힙에 값 존재할 때
                    visited[heap_min[0][1]] = False  # 최대 힙과 공유하는 visited의 인덱스 False로 바꿔줌
                    heapq.heappop(heap_min)  # 최소 힙에서 값 뺌

    if True not in visited:  # visited에 True가 없다는 건 힙에 값이 없다는 것
        print("EMPTY")
    else:
        # 정수가 있다면
        # 연산이 끝난 후 제거 되지 못한 최대 힙과 최소 힙을 팝하여 제거
        while heap_max and visited[heap_max[0][1]] == False:
            heapq.heappop(heap_max)
        while heap_min and visited[heap_min[0][1]] == False:
            heapq.heappop(heap_min)

        print(-heap_max[0][0], heap_min[0][0])



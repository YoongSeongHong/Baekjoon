import sys

T = int(sys.stdin.readline())
for i in range(T):
    n, turn = map(int, sys.stdin.readline().split())
    pri = list(map(int, sys.stdin.readline().split()))
    queue = [0] * n
    queue[turn] = 1
    result = 0
    while(len(pri) != 0):
        G = max(pri)
        if(pri[0] == G):
            pri.pop(0)
            n = queue.pop(0)
            result += 1
            if(n == 1):
                print(result)
                break

        else:
            pri.append(pri.pop(0))
            queue.append(queue.pop(0))
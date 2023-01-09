import sys

N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(h)
while start <= end:
    cut = 0
    mid = (start + end) // 2
    for hs in h:
        if hs > mid:
            cut += hs - mid

    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)


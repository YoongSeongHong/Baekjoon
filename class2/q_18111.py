# 18111번 마인크래프트
import sys

N, M, B = map(int, sys.stdin.readline().split())
lst1 = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst1 = lst1 + a

mx = max(lst1)
mn = min(lst1)
times = []

for i in range(mn, mx+1):
    lst2 = lst1.copy()
    block = B
    time = 0
    flag = 0
    for j in range(len(lst2)):
        if lst2[j] > i:
            get = lst2[j] - i
            lst2[j] = i
            time += 2*get
            block += get
    for k in range(len(lst2)):
        if lst2[k] < i:
            use = i - lst2[k]
            lst2[k] = i
            block -= use
            time += 1*use
        if block < 0:
            flag = 1
            break
    if flag == 0:
        l = [time, i]
        times.append(l)
times = sorted(times, key=lambda times: times[1], reverse=True)
times = sorted(times, key=lambda times: times[0])
print(times[0][0], times[0][1])

import sys

N = int(sys.stdin.readline())
flag = 0
for i in range(1, N+1):
    s = i
    li = list(map(int, str(i)))
    s += sum(li)
    if(s == N):
        flag = i
        break
print(flag)
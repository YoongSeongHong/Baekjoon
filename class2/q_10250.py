import sys

T = int(sys.stdin.readline())
lst = []
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H != 0:
        floor = N % H
        room = N // H + 1
    else:
        floor = H
        room = N // H
    arr = []
    arr.append(str(floor))
    arr.append(str(room))
    if room <= 9:
        s = '0'.join(arr)
    else:
        s = ''.join(arr)
    print(s)
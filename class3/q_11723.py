# 11723번 집합
import sys


# 명령이 add 인 경우
def s_add(x):
    S.add(x)


# 명령이 remove 인 경우
def s_remove(x):
    S.discard(x)


# 명령이 check 인 경우
def s_check(x):
    if x in S:
        print(1)
    else:
        print(0)


# 명령이 toggle 인 경우
def s_toggle(x):
    if x in S:
        S.discard(x)
    else:
        S.add(x)


M = int(sys.stdin.readline())
S = set()
for i in range(M):
    arr = list(sys.stdin.readline().split())

    if len(arr) == 2:
        arr[1] = int(arr[1])
        if arr[0] == 'add':
            s_add(arr[1])
        elif arr[0] == 'remove':
            s_remove(arr[1])
        elif arr[0] == 'check':
            s_check(arr[1])
        elif arr[0] == 'toggle':
            s_toggle(arr[1])
    else:
        # 명령이 all 인 경우
        if arr[0] == 'all':
            S = set((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
        # 명령이 empty 인 겨우
        elif arr[0] == 'empty':
            S = set()



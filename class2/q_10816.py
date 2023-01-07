import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
hash = {}
for i in n_list:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in m_list:
    if i in hash:
        print(hash[i])
    else:
        print(0)

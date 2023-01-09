import sys

N, K = map(int, sys.stdin.readline().split())

n1 = 1
n2 = 1
for i in range(K):
    n1 *= (N-i)
for i in range(K):
    n2 *= (i+1)
print(n1//n2)
# 1764번 듣보잡
import sys

N, M = map(int, sys.stdin.readline().split())
not_hear = []
not_see = []
for i in range(N):
    name = sys.stdin.readline().rstrip()
    not_hear.append(name)
for i in range(M):
    name = sys.stdin.readline().rstrip()
    not_see.append(name)
not_see_hear = list(set(not_hear) & set(not_see))

not_see_hear.sort()
print(len(not_see_hear))
for i in range(len(not_see_hear)):
    print(not_see_hear[i])

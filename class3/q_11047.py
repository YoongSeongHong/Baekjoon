# 11047번 동전 0
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dq = deque()
for i in range(N):
    v = int(sys.stdin.readline())
    if v <= K:  # 어차피 K보다 큰 동전은 쓰일 일이 없다.
        dq.append(v)

count = 0  # 동전 개수 세는 변수
for i in range(len(dq)):
    n = dq.pop()  # 가장 비싼 동전 부터 최대한 쓰기
    count += K // n  # 쓴 동전 갯수만큼 count +
    K = K % n  # 동전 쓴 만큼 K는 그 나머지로 최신화
print(count)

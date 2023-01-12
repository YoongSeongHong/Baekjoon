# 2579번 계단 오르기
import sys

floor = int(sys.stdin.readline())
lst = []
dp = [0] * floor
for i in range(floor):
    score = int(sys.stdin.readline())
    lst.append(score)

dp[0] = lst[0]
# floor >1, floor >2 조건 안 걸면 인덱스 에러 뜸
if floor > 1:
    dp[1] = max(lst[0]+lst[1], lst[1])
if floor > 2:
    dp[2] = max(lst[0]+lst[2], lst[1]+lst[2])
    for i in range(3, floor):
        # i-1을 밟는 경우: i-2는 밟으면 안 되니까 i-3까지의 dp 구하고 i-1, i 점수 더해 주기
        # i-2를 밟는 경우: i-2까지의 dp랑 i 점수 더해 주면 됨
        dp[i] = max(lst[i-1] + dp[i-3] + lst[i], dp[i-2] + lst[i])
print(dp[floor-1])
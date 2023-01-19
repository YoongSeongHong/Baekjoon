# 9095번 1,2,3 더하기
import sys

T = int(sys.stdin.readline())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    # i-1 i-2 i-3 인 경우 에서 각각 +1 +2 +3 인 경우 들만 더해 주면 된다.
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for i in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])

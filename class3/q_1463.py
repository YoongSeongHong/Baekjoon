# 1463번 1로 만들기
import sys

N = int(sys.stdin.readline())
time = 0
dp = [0] * (N + 1)
if N >= 2:
    dp[1] = 1
if N >= 3:
    dp[2] = 1
if N > 3:
    for i in range(3, N+1):
        if (i+1) % 6 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i//3] + 1)
        elif (i+1) % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
        elif (i+1) % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
        else:
            dp[i] = dp[i-1] + 1
print(dp[N-1])

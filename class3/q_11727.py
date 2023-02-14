# 11727번 2xn 타일링2
import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
if n >= 2:
    # n에 1 입력하는 경우 예외처리
    dp[2] = 3
    for i in range(3, n+1):
        # 점화식
        dp[i] = dp[i-2]*2 + dp[i-1]
print(dp[n] % 10007)
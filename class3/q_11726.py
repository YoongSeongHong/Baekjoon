# 11726번 2xn 타일링
import sys

# 그냥 dp 문제
n = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2]
# 10007로 나눈 나머지 출력하는게 문제
print(dp[n] % 10007)

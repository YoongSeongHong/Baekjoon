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
        # dp 이용, 6 나눠 지면 i를 3, 2로 나눈 i dp 중 최솟값 이용
        if (i+1) % 6 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i//3] + 1)
        # 6으로 안 나눠 지고 2으로 나눠 지면 i를 2로 나눈 값이랑 바로 앞 dp 값 중 최솟값 이용
        elif (i+1) % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
        # 6으로 안 나눠 지고 3으로 나눠 지면 i를 3으로 나눈 값이랑 바로 앞 dp 값 중 최솟값 이용
        elif (i+1) % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
        # 그것도 아니면 이전 dp 값의 + 1
        else:
            dp[i] = dp[i-1] + 1
print(dp[N-1])

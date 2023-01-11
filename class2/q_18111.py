# 18111번 마인크래프트
import sys

N, M, B = map(int, sys.stdin.readline().split())
lst1 = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst1 = lst1 + a

mx = max(lst1)
mn = min(lst1)
# 리스트 정렬 안하면 시간 초과 뜸
lst1.sort(reverse=True)

result_sec = 9999999999
result_h = 0

# 최솟값 부터 최댓값 까지 다 돌려 볼거
for i in range(mn, mx+1):
    block = B
    time = 0
    for j in lst1:
        # 원하는 층 수 보다 높게 쌓여 있으면 캐기
        if j > i:
            get = j - i
            time += 2*get
            block += get
        # 원하는 층 수 보다 낮게 쌓여 있으면 쌓기
        elif j < i:
            use = i - j
            block -= use
            time += use
    # 블록 개수 안 모자라고 result_sec 보다 적게 걸리면 갱신. 같은 초 나와도 층 수 높은 값으로 갱신 하는 구조
    if block >= 0 and result_sec >= time:
        result_h = i
        result_sec = time
print(result_sec, result_h)

# 2805번 나무자르기
import sys

# N은 나무의 수, M은 상근이가 원하는 나무 길이
N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(h)  # 제일 길이가 긴 나무의 길이
while start <= end:  # 이진 탐색, 시작점 끝점 만날 때까지
    cut = 0  # 잘린 길이
    mid = (start + end) // 2  # 중간값 설정(자르기로 한 높이)
    for hs in h:
        if hs > mid:  # 지정한 길이보다 길어야 자를 수 있음
            cut += hs - mid

    if cut >= M:  # 잘린 길이가 M보다 길면 -> 중간값 다음값으로 시작점 설정해서 더 윗부분 검사
        start = mid + 1
    else:  # 잘린 길이가 M보다 짧으면 -> 중간값 이전값으로 끝점 설정해서 더 아랫부분 검사
        end = mid - 1

print(end)


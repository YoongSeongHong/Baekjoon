# 1931번 회의실 배정
import sys

N = int(sys.stdin.readline())
# 시작, 끝 시간을 이차원 배열로 선언
arr = [[0]*2 for _ in range(N)]

# 시작, 끝 시간을 이차원 배열엘 저장
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    if start < mn:
        mn = start
    if mx < end:
        mx = end
    arr[i][0] = start
    arr[i][1] = end

# 그리디 알고리즘 - 끝나는 시간 오름차순으로 정렬하고, 그 중 시작 시간을 오름차순 정렬
arr.sort(key=lambda x: (x[1], x[0]))

# 맨 처음 값부터 시작하므로 count는 1부터 시작, 제일 마지막으로 끝난 시각을 final에 저장
count = 1
final = arr[0][1]

# 다음 회의가 시작 시간이 이전 회의 끝 시간 이후이면 그 회의 진행
for i in range(1, N):
    if arr[i][0] >= final:
        final = arr[i][1]
        count += 1

print(count)

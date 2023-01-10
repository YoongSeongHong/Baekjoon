#1654번 랜선 자르기
import sys

K, N = map(int, sys.stdin.readline().split())
arr = []
for i in range(K):
    n = int(sys.stdin.readline())
    arr.append(n)

end = max(arr) #잘릴 수 있는 최고의 값은 가장 긴 랜선의 길이
start = 1
while start <= end: #자를 값을 이분탐색으로  찾기
    mid = (end + start) // 2
    count = 0
    for i in range(K):
        n = arr[i] // mid
        count += n

    # ex) 11개보다 크거나 같게 나오면 자를 랜선의 길이가 mid 값보다 큰 것
    # 11이 되었을때 break해도 구할순있을거같지만 11개를 만드는 값 중 최대 값이 아닐 수도 있음

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)



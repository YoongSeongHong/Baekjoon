# 18870번 좌표 압축
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 중복 원소 제거 (궁금한 값보다 작은 서로 다른 원소 수 구하므로 중복값 필요없음)
s = set(arr)
arr2 = list(s)

# 정렬하면 자연스럽게 그 인덱스 값이 본인보다 작은 서로 다른 원소 수가 된다.
arr2.sort()
dict = {}
for i in range(len(arr2)):
    dict[arr2[i]] = i
for i in arr:
    print(dict[i], end=' ')
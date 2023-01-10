# 2108번 통계학
import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)

# 산술평균
s = sum(lst) / N
print(round(s))

# 중앙값
lst.sort()
print(lst[N//2])

# 최빈값
d = {string: 0 for string in lst}
# 리스트 원소 들을 키로, 그 갯수를 값으로 가지는 딕셔너리 생성
for i in range(N):
    if lst[i] in d.keys():
        d[lst[i]] += 1
# 가장 큰 값을 가지는 키들 따로 배열 저장
fq = [k for k, v in d.items() if max(d.values()) == v]
# 최빈값 여러 개인 경우 두 번째로 작은 값 출력
if len(fq) > 1:
    fq.sort()
    print(fq[1])
# 최빈값 한 개인 경우
else:
    print(fq[0])

# 범위
mx = max(lst)
mn = min(lst)
print(mx - mn)
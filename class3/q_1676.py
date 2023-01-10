# 1676번 팩토리얼 0의 개수
import sys

N = int(sys.stdin.readline())
mul = 1

# 팩토리얼 구하기
for i in range(N):
    mul *= i+1


lst = list(str(mul))
index = len(lst)-1
count = 0
# 끝에서 부터 0이 아닌 값이 나올 때까지 검사 하면서 count 1씩 증가
while lst[index] == '0':
    count += 1
    index -= 1
print(count)
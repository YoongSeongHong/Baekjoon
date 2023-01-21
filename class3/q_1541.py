# 1541번 잃어버린 괄호
import sys

s = sys.stdin.readline()
arr = []
nn = ''
for n in s:  # 식에서 숫자, +, - 분리 하여 리스트 에 저장
    if n == '-':  # -나오기 전 까지 숫자는 합치고, -는 따로 저장
        arr.append(int(nn))
        arr.append('-')
        nn = ''
    elif n == '+':  # +나오기 전 까지 숫자는 합치고, +는 따로 저장
        arr.append(int(nn))
        arr.append('+')
        nn = ''
    else:  # 연속 되는 숫자는 합침
        nn += n
arr.append(int(nn.rstrip()))

# 최솟값이 나오게 하려면 식에 있는 더하기 를 먼저 처리 하고 주루룩 빼면 됨 (가장 큰 값을 빼게 됨)
arr2 = []
while len(arr) != 0:
    if arr[0] == '+':
        arr.pop(0)
        arr2.append(arr2.pop() + arr.pop(0))
    else:
        arr2.append(arr.pop(0))

# 남아 있는 식은 빼기만 존재. 그 식을 계산 하기만 하면 최솟값(최적의 해)이 나온다.
result = arr2.pop(0)
while len(arr2) > 1:
    arr2.pop(0)
    result -= arr2.pop(0)
print(result)





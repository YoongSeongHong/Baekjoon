# 1003번 피보나치 함수
import sys


def fibonacci(num):
    length = len(zero)
    # 0, 1 개수 각각의 점화 식은 f[i] = f[i-1] + f[i-2]
    if length <= num:
        for j in range(length, num+1):
            zero.append(zero[j-1] + zero[j-2])
            one.append(one[j-1] + one[j-2])


T = int(sys.stdin.readline())
# 미리 0, 1의 인덱스 0, 1, 2번 채워 놓음
zero = [1, 0, 1]
one = [0, 1, 1]
for i in range(T):
    n = int(sys.stdin.readline())
    fibonacci(n)
    print(zero[n], one[n])
import sys

n = int(sys.stdin.readline()) #3, 5킬로
count = 0
while n >= 0:
    if n % 5 == 0:
        print(n // 5 + count)
        exit(0)
    else:
        n -= 3
        count += 1

print(-1)

import sys

n = int(sys.stdin.readline())
start = 1
count = 1
while(True):
    if (n <= start):
        break
    start = start + (count * 6)
    count += 1

print(count)
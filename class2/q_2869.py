import sys

A, B, V = map(int, sys.stdin.readline().split())
one_day = A - B
until = V - A
day = until // one_day
if until % one_day == 0:
    day += 1
else:
    day += 2
print(day)
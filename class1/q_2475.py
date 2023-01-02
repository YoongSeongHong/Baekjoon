import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())
a2, b2, c2, d2, e2 = a**2, b**2, c**2, d**2, e**2

print((a2+b2+c2+d2+e2)%10)
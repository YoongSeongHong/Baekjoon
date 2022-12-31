import sys

arr = [-1]*26
s = sys.stdin.readline()
for i in range(26):
    ch = chr(i+97)
    n = s.find(ch)
    print(n, end=' ')

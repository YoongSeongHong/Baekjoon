import sys

n = int(sys.stdin.readline())
if(n <= 100 and 90 <= n):
    print('A')
elif(n >= 80):
    print('B')
elif(n >= 70):
    print('C')
elif(n >= 60):
    print('D')
else:
    print('F')
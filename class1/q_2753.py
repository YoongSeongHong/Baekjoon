import sys

n = int(sys.stdin.readline())
if(n % 4 == 0 and n % 100 != 0):#4의 배수이면서 100의 배수가 아닐때
    print('1')
elif(n % 400 == 0):
    print('1')
else:
    print('0')
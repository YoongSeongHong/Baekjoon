import sys

def calMax(n1, n2):
    arr1 = []
    arr2 = []
    for i in range(1, n1 + 1):
        if(n1 % i == 0):
            arr1.append(i)
    for i in range(1, n2 + 1):
        if(n2 % i == 0):
            arr2.append(i)
    s1 = set(arr1)
    s2 = set(arr2)
    print(max(s1 & s2))

def calMin(n1, n2):
    if(n1 >= n2):
        big = n1
    else:
        big = n2
    for i in range(big, (n1*n2)+1):
        if(i % n1 == 0 and i % n2 == 0):
            result = i
            break
    print(result)

n1, n2 = map(int, sys.stdin.readline().split())
calMax(n1, n2)
calMin(n1, n2)



import sys
T = int(sys.stdin.readline())
arr1 = []
arr2 = []
for i in range(T):
    a, b = map(str, sys.stdin.readline().split())
    n = int(a)
    arr1.append(n)
    arr2.append(b)

arrLen = len(arr1)
for i in range(arrLen):
    arr3 = list(arr2[i])
    for j in arr3:
        for k in range(arr1[i]):
            print(j, end='')
    print('')
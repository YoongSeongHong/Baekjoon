import sys
arr = []
for i in range(10):
    n = int(sys.stdin.readline())
    r = n % 42
    arr.append(r)

arr2 = []
arr2.append(arr.pop())
for i in range(9):
    n = arr.pop()
    flag = 0
    for i in range(len(arr2)):
        if(arr2[i] == n):
            flag = 1
    if(flag == 0):
        arr2.append(n)
print(len(arr2))
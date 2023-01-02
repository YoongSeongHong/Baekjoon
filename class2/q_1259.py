import sys

arr = []
while(True):
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    arr.append(n)

for i in range(len(arr)):
    arr2 = list(map(int, str(arr[i])))
    l = len(arr2) // 2
    arr3 = []
    for i in range(l):
        arr3.append(arr2.pop())
    flag = 0
    for i in range(l):
        if(arr2[i] != arr3[i]):
            flag = 1
    if(flag == 1):
        print("no")
    else:
        print('yes')


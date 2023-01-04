import sys

arr = []
while(True):
    n1, n2, n3 = map(int, sys.stdin.readline().split())
    if(n1 == 0 and n2 == 0 and n3 == 0):
        break
    arr.append([n1, n2, n3])

for i in range(len(arr)):
    big = max(arr[i])
    arr[i].remove(big)
    n = ((arr[i][0])**2) + ((arr[i][1]**2))
    if(n == big**2):
        print("right")
    else:
        print("wrong")

import sys
N = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip()
arr = list((map(int, st)))
sum = 0
for i in range(len(arr)):
    sum += arr[i]
print(sum)
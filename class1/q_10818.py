import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
min = nums[0]
max = nums[0]
for i in range(1, n):
    if(nums[i] < min):
        min = nums[i]
    elif(nums[i] > max):
        max = nums[i]
print(min, max)
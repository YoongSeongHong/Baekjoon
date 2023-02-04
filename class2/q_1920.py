import sys


def search(num):
    left = 0
    right = arr_len - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return True

        if num < arr[mid]:
            right = mid - 1
        elif num > arr[mid]:
            left = mid + 1


arr_len = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

arr_len = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(count):

    if search(nums[i]):
        print(1)
    else:
        print(0)


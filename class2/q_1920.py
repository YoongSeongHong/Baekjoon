import sys
<<<<<<< HEAD
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
=======

arr_len = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
>>>>>>> ef9a750aabf6cdc1fb597e66bcb7cc28e4e6a87e

count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

<<<<<<< HEAD
for i in range(count):

    if search(nums[i]):
        print(1)
    else:
        print(0)
=======
# for i in range(count):
#     flag = 0
#     for j in range(arr_len):
#         if nums[i] == arr[j]:
#             print(1)
#             flag = 1
#     if flag == 0:
#         print(0)


>>>>>>> ef9a750aabf6cdc1fb597e66bcb7cc28e4e6a87e

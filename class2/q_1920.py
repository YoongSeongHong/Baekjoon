# 1920번 수찾기
import sys


def search(num):  # 이진 탐색 함수
    left = 0  # 맨 왼쪽은 0부터 시작
    right = arr_len - 1  # 맨 오른쪽은 마지막부터 시작
    while left <= right:  # left, right 엇갈리면 검사 끝난거
        mid = (left + right) // 2  # 중간 값
        if arr[mid] == num:  # 중간 값 검사해서 찾는 수면 True 리턴
            return True

        if num < arr[mid]:  # 찾는 값이 중간값보다 왼쪽이면
            right = mid - 1  # 맨 오른쪽 값을 중간값 이전값으로 설정
        elif num > arr[mid]:  # 찾는 값이 중간값보다 오른쪽이면
            left = mid + 1  # 맨 왼쪽 값을 중간값 다음값으로 설정


# 배열 입력받고 정렬
arr_len = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

# 있는지 검사할 수 입력받기
count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(count):

    if search(nums[i]):  # 있으면
        print(1)
    else:  # 없으면
        print(0)


# 10816번 숫자 카드 2 이분 탐색 이용
import sys

N = sys.stdin.readline()
n_list = sorted(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
m_list = map(int, sys.stdin.readline().split())


def binary(n, n_list, start, end):  # 이진 탐색 함수
    if start > end:  # 찾는 값 없으면 0 리턴
        return 0
    m = (start+end)//2  # 중간값 설정
    if n == n_list[m]:  # 중간값이 찾는 값이면
        return n_list[start:end+1].count(n)  # 최대한 쪼갠 범위 내에서 count
    elif n < n_list[m]:  # 중간값이 찾는 값보다 오른쪽에 있으면
        return binary(n, n_list, start, m-1)  # 끝 값을 중간값 -1 로 설정
    else:  # 중간값이 찾는 값보다 왼쪽에 있으면
        return binary(n, n_list, m+1, end)  # 시작 값을 중간값 +1 로 설정


n_dic = {}  # 딕셔너리에 키: 궁금한 숫자 , 값: 개수로 설정
for n in n_list:
    start = 0 # 시작점 설정
    end = len(n_list) - 1  # 끝점 설정
    if n not in n_dic:
        n_dic[n] = binary(n, n_list, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in m_list))


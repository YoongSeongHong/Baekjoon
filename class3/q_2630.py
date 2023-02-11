# 2630번 색종이 만들기
import sys


def division(x, y, N):
    # color에 첫번째 색깔 지정해서 for문 돌리고 다른색상이 나오면 다시 분리
    color = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                division(x, y, N//2)  # 좌표로 나누면 2사분면
                division(x, y+N//2, N//2)  # " 3사분면
                division(x+N//2, y, N//2)  # " 1사분면
                division(x+N//2, y+N//2, N//2)  # " 4사분면
                return  # 리턴 안해주면 1, 0 계속 추가함
    if color == 1:  # 파란 종이
        cnt.append(1)
    elif color == 0:  # 하얀 종이
        cnt.append(0)


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    arr.append(row)
cnt = []  # 1은 파란색, 0은 하얀색 종이 저장
division(0, 0, N)  # (0,0) 부터 시작
print(cnt.count(0))
print(cnt.count(1))
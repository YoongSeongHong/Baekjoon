import sys


def cal(floor, roomNum):
    # if(floor == 0):
    #     return roomNum
    # if(roomNum == 0):
    #     return 0
    # return cal(floor-1, roomNum) + cal(floor, roomNum-1)
    arr = [[0 for col in range(roomNum)] for row in range(floor+1)]
    for i in range(0, roomNum):
        arr[0][i] = i+1

    for i in range(1, floor+1):
        for j in range(roomNum):
            if(j == 0):
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[floor][roomNum-1]


T = int(sys.stdin.readline())
arr1 = []
arr2 = []

for i in range(T):
    floor = int(sys.stdin.readline())
    roomNum = int(sys.stdin.readline())
    arr1.append(floor)
    arr2.append(roomNum)

for i in range(T):
    print(cal(arr1[i], arr2[i]))
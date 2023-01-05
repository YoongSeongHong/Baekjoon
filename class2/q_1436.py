import sys

n = int(sys.stdin.readline())
temp = 1
turn = 0
end = "666"
while(True):
    s = str(temp)
    if(end in s):
        turn += 1
    if(turn == n):
        print(temp)
        break
    temp += 1
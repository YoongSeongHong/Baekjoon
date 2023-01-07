import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
chess1 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
chess2 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]

for i in range(N):
    s = sys.stdin.readline().rstrip()
    lst.append(s)
s = []
for i in range(N-7): #height
    for j in range(M-7): #width
        be1 = 0
        be2 = 0
        for k in range(i, 8 + i): #height
            for l in range(j, 8 + j): #width
                if lst[k][l] != chess1[k-i][l-j]:
                    be1 += 1
                if lst[k][l] != chess2[k-i][l-j]:
                    be2 += 1
        smaller = min(be1, be2)
        s.append(smaller)
print(min(s))




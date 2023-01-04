import sys

T = int(sys.stdin.readline())
stack = []
for i in range(T):
    arr = list(map(str, sys.stdin.readline().split()))
    if(len(arr) == 2):
        stack.append(int(arr[1]))
    elif(arr[0] == "pop"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif(arr[0] == "size"):
        print(len(stack))
    elif(arr[0] == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(arr[0] == "top"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack)-1])

import sys

T = int(sys.stdin.readline())
queue = []
for i in range(T):
    arr = list(map(str, sys.stdin.readline().split()))
    if(len(arr) == 2):
        if(arr[0] == "push_front"):
            queue.insert(0, int(arr[1]))
        elif(arr[0] == "push_back"):
            queue.append(int(arr[1]))

    elif(arr[0] == "pop_front"):
        if(len(queue) == 0):
            print(-1)
        else:
            n = queue[0]
            del queue[0]
            print(n)
    elif(arr[0] == "pop_back"):
        if(len(queue) == 0):
            print(-1)
        else:
            n = queue[len(queue)-1]
            del queue[len(queue)-1]
            print(n)
    elif(arr[0] == "size"):
        print(len(queue))
    elif(arr[0] == "empty"):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif(arr[0] == "front"):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
    elif(arr[0] == "back"):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[len(queue)-1])


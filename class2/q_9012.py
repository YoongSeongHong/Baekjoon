import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = list(sys.stdin.readline().rstrip())
    if(len(a) % 2 == 1):
        print("NO")
    else:
        stack = []
        for i in range(len(a)):
            stack.append(a[i])
            try:
                if stack[-2]+stack[-1] == "()":
                    stack.pop()
                    stack.pop()
            except:
                continue
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

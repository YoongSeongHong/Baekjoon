import sys

arr = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    arr.append(s)

for i in range(len(arr)):
    stack = []
    for j in range(len(arr[i])):
        if arr[i][j] == '(' or arr[i][j] == ')' or arr[i][j] == '[' or arr[i][j] == ']':
            stack.append(arr[i][j])
        try:
            if stack[-2] + stack[-1] == "()" or stack[-2] + stack[-1] == "[]":
                stack.pop()
                stack.pop()
        except:
            continue

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
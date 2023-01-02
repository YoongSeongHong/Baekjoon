ns = input()
arr = ns.split()
arrLen = len(arr)
for i in range(arrLen):
    arr[i] = int(arr[i])

down = 0
up = 0

for i in range(arrLen - 1):
    if(arr[i] < arr[i+1]):
        up += 1
    else:
        down += 1

if(down == 7):
    print("descending")
elif(up == 7):
    print("ascending")
else:
    print("mixed")
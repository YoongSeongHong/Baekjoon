n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(input())

for i in range(n):
    score = 0
    weight = 0
    result = list(arr1[i])
    arrLen = len(arr1[i])
    for j in range(arrLen):
        if(result[j] == 'O'):
            weight += 1
            score += weight
        elif(result[j] == 'X'):
            weight = 0
    arr2.append(score)

for i in range(n):
    print(arr2[i])
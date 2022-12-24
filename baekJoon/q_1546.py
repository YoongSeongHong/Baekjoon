n = int(input())
scores = input()
arr = scores.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

big = arr[0]
for i in arr:
    if(i > big):
        big = i

for i in range(len(arr)):
    arr[i] = arr[i] / big * 100
sum = 0
for i in arr:
    sum += i

print(sum / n)

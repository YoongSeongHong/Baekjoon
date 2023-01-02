arr = []
for i in range(9):
    a = input()
    arr.append(int(a))
biggest = arr[0]
biggest_index = 0
for i in range(9):
    if(biggest < arr[i]):
        biggest = arr[i]
        biggest_index = i

print(biggest)
print(biggest_index + 1)
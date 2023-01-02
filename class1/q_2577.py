A = input() #150
B = input() #266
C = input() #427
result = int(A) * int(B) * int(C)
a = []
for i in str(result):
    a.append(i)
b = [0] * 10
for i in range(10):
    for j in a:
        if int(j) == i:
            b[i] += 1

for i in range(10):
    print(b[i])


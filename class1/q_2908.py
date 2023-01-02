ipn1, ipn2 = input().split()

arr1 = list(ipn1)
re_arr1 = []
while(len(arr1) != 0):
    n = arr1.pop()
    re_arr1.append(n)

arr2 = list(ipn2)
re_arr2 = []
while(len(arr2) != 0):
    n = arr2.pop()
    re_arr2.append(n)

num1 = int(''.join(re_arr1))
num2 = int(''.join(re_arr2))

if(num1 > num2):
    print(num1)
else:
    print(num2)
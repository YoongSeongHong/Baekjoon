a = input()
a_upper = a.upper()
arr = []
dic = {}
for alp in a_upper:
    dic.setdefault(alp, 0)
    arr.append(alp)

for alp1 in dic:
    for alp2 in arr:
        if alp2 == alp1:
            dic[alp1] = dic[alp1] + 1

ma = max(dic.values())
arr2 = []
for i in dic:
    if(dic.get(i) == ma):
        arr2.append(i)
if(len(arr2) > 1):
    print("?")
else:
    print(max(dic, key=dic.get))


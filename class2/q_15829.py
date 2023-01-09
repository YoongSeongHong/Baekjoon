import sys

def hashin(L, s):
    hash_value = 0
    for i in range(L):
        hash_value += (ord(s[i])-96) * (31**i)
        hash_value = hash_value % 1234567891
    return hash_value



L = int(sys.stdin.readline())
s = sys.stdin.readline()
print(hashin(L, s))

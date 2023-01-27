# 1620번 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, sys.stdin.readline().split())
hash = {}
for i in range(1, N+1):  # 키에 번호, 값에 포켓몬 명 저장
    name = sys.stdin.readline().rstrip()
    hash[str(i)] = name

hash2 = {v: k for k, v in hash.items()}  # hash1에서 키, 값 서로 뒤집은 딕셔너리
for i in range(M):
    quiz = sys.stdin.readline().rstrip()
    if quiz in hash.keys():  # 문제가 hash 키(번호) 중에 있으면 그 값(이름) 출력
        print(hash[quiz])
    elif quiz in hash2.keys():  # 문제가 hash2 키(이름) 중에 있으면 그 값(번호) 출력
        print(hash2[quiz])


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_n = {}  # {'25': 'Pikachu'}
dic_s = {}  # {'Pikachu': 25}
for i in range(N):
    value = input().rstrip()
    dic_n[str(i+1)] = value
    dic_s[value] = i+1

for j in range(M):
    quest = input().rstrip()
    if quest.isdigit():  # 문자인지 숫자인지 판별하는 함수
        print(dic_n[quest])
    if quest.isalpha():  # 문자인지 숫자인지 판별하는 함수
        print(dic_s[quest])
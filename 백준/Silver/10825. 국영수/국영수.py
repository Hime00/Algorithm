import sys,time,copy
input = sys.stdin.readline
from collections import deque

n=int(input())
array=[list(input().split()) for _ in range(n)]

array.sort(key=lambda x:x[0])
array.sort(key=lambda x:int(x[3]),reverse=True)
array.sort(key=lambda x:int(x[2]))
array.sort(key=lambda x:int(x[1]),reverse=True)

for i in range(n):print(array[i][0])
from itertools import combinations
import sys
input=sys.stdin.readline
while True:
  data=list(map(int,input().split()))
  if data==[0]:
    break
  k=data[0]
  del data[0]
  s=list(combinations(data,6))
  for i in s:
    for j in i:
      print(j,end=' ')
    print()
  print()
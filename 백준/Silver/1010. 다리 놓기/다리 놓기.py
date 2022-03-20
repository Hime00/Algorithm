import math
case=int(input())
for i in range(case):
  n,m=map(int,input().split())
  print(math.factorial(m)//(math.factorial(m-n)*math.factorial(n)))
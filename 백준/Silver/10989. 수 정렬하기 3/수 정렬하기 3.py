import sys
n=int(input())
count=[0]*(10001)
for _ in range(n):
  k=int(sys.stdin.readline())
  count[k]+=1
for i in range(10001):
  for j in range(count[i]):
    print(i)
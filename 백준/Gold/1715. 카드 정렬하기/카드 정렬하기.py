import heapq,sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
data=[]
h=[]
for i in range(n):
  heapq.heappush(h,int(input()))

result=0
while len(h)!=1:
  a=heapq.heappop(h)
  b=heapq.heappop(h)
  sum=a+b
  result+=sum
  heapq.heappush(h,sum)
print(result)
import sys
input=sys.stdin.readline
k=int(input())
data=[]
for i in range(k):
  item=int(input())
  if item:
    data.append(item)
  else:
    data.pop()
print(sum(data))
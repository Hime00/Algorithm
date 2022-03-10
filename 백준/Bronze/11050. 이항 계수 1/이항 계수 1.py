from itertools import combinations
n,k=map(int,input().split())
array=[]
for i in range(n):
  array.append(i)
k=list(combinations(array,k))
print(len(k))
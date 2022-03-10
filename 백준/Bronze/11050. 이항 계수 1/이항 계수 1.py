from itertools import combinations
n,k=map(int,input().split())
array=[]
for i in range(n):
  array.append(i)
# 앞에 list를 붙여야 함
k=list(combinations(array,k))
print(len(k))

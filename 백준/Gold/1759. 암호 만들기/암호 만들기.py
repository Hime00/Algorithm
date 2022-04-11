from itertools import combinations
L,C=map(int,input().split())
data=list(input().split())
data.sort()
result=list(combinations(data,L))
def check(i):
    index=0
    a=0
    b=0
    while True:
        if index==L:
          break
        if i[index]=="a" or i[index]=="e" or i[index]=="i" or  i[index]=="o" or i[index]=="u":
          a+=1
        else:
          b+=1
        if a >= 1 and b>=2:
          return 1
          break
        index+=1
    return 0
for i in result:
  k=check(i)
  if k:
    print(''.join(i))
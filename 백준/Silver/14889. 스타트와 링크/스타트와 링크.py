n = int(input())
data=[list(map(int,input().split())) for _ in range(n)]
first=[]
second=[]
def go(index,first,second):
  result=-100
  if index==n:
    if len(first)!=n//2:
      return -1
    if len(second)!=n//2:
      return -1
    else:
      a=0
      b=0
      for i in range(n//2):
        for j in range(n//2):
          if i==j:
            continue
          a+=data[first[i]][first[j]]
          b+=data[second[i]][second[j]]
      return abs(a-b)
  if len(first)>n//2:
    return -1
  if len(second)>n//2:
    return -1
  result=-1
  t1=go(index+1,first+[index],second)
  if result == -1 or (t1 != -1 and result > t1 ):
    result=t1
  
  t2=go(index+1,first,second+[index])
  if result == -1 or (t2 != -1 and result > t2 ):
    result=t2
  return result


  
print(go(0,first,second))
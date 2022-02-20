a,b=map(int,input().split())
array = [[] for _ in range(a+1)]
for _ in range(b):
    x, y = map(int, input().split())		
    array[x].append(y)
    array[y].append(x)
visited=[0 for _ in range(a+1)]
def dfs(x):
  visited[x]=1
  for i in array[x]:
# 방문하지 않은 정점만 1로 만들면 되므로        
    if visited[i]==0:
      dfs(i)
  return True
result=0
for i in range(1,a+1):
# 방문하지 않은 정점에 대하여
  if visited[i]==0:
    dfs(i)
    result+=1
print(result)

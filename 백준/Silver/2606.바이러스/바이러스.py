a=int(input())
b=int(input())
array = [[] for _ in range(a+1)]
for _ in range(b):
    x, y = map(int, input().split())		
    array[x].append(y)
    array[y].append(x)
visited=[0 for _ in range(a+1)]
def dfs(array,x):
  visited[x]=1
  for i in array[x]:
    if visited[i]==0:
      dfs(array,i)
  return True
dfs(array,1)
print(sum(visited)-1)
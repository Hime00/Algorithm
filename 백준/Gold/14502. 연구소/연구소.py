import sys,copy
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
resultArray=[]
zero=[]
virus=[]
for i in range(n) :
    for j in range(m):
        if array[i][j] == 0:
            zero.append([i,j])
        elif array[i][j] == 2:
            virus.append([i,j])
# 0의 위치들에 대한 조합들을 저장          
k=list(combinations(zero,3))

def dfs(x, y):
    array_[x][y]=2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and array_[nx][ny] == 0:
            dfs(nx,ny)
    return
a=0
def getResult(array):
    result=0
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                result+=1
    return result
for i in k:
    array_ = copy.deepcopy(array)
    array_[i[0][0]][i[0][1]] = 1
    array_[i[1][0]][i[1][1]] = 1
    array_[i[2][0]][i[2][1]] = 1
    for v in virus :
        dfs(v[0],v[1])
    resultArray.append(getResult(array_))    
    a+=1
print(max(resultArray))
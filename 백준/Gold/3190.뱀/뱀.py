from collections import deque
n=int(input())
k=int(input())
array=[]
queue=deque()
rotate_x=[0,1,0,-1]
rotate_y=[1,0,-1,0]

game=[[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
    g,h=map(int,input().split())
    game[g-1][h-1]=1
l=int(input())
for i in range(l):
    array.append(list(input().split()))
    
x=0
y=0
cur=0
result=0
next_x=x
next_y=y+1
queue.append([0,0])
def check():
    for i in array:
        if result==int(i[0]):
            return i[1]
    return -1
while True:
    result += 1
    if [next_x,next_y] in queue:
        break
    if next_y>=n or next_y<0 or next_x>=n or next_x<0 :
        break
    queue.append([next_x,next_y])
    if game[next_x][next_y] == 0:
        queue.popleft()
    elif game[next_x][next_y] == 1:
        game[next_x][next_y] = 0
    prev_x=x
    prev_y=y
    x = next_x
    y = next_y
    k = check()
    if k != -1:
        if k == 'D':
            cur += 1
            next_x = x + rotate_x[cur % 4]
            next_y = y + rotate_y[cur % 4]
        elif k == 'L':
            cur -= 1
            next_x = x + rotate_x[cur % 4]
            next_y = y + rotate_y[cur % 4]
    else:
        next_x = x + rotate_x[cur % 4]
        next_y = y + rotate_y[cur % 4]
print(result)
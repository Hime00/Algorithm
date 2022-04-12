n = int(input())
ans = 0
row = [0] * n
check= [0]*n
def is_promising(x):
    for i in range(x):
        if abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
      # [x, i]에 퀸을 놓겠다.
      if not check[i]:
        row[x] = i
      # Backtracking으로 완전탐색보다 경우의수를 줄인다
        if is_promising(x):
          check[i]=1
          n_queens(x+1)
          check[i]=0
n_queens(0)
print(ans)
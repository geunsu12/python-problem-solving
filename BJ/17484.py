N, M = map(int,input().split())
rocket = []

for j in range(N):
    rocket.append(list(map(int,input().split())))
ans = 999999

dx = [-1,0,1]

def dfs(y,x,fuel,k):
    global ans
    if y == N-1:
        ans = min(ans,fuel)
        return
    ny = y+1
    for i in range(3):
        if i != k:
            nx = x + dx[i]
            if 0<=nx<M:
                dfs(ny,nx,fuel+rocket[ny][nx],i)

for m in range(M):
    dfs(0,m,rocket[0][m],4)

print(ans)

import copy
n,m = map(int,input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int,input().split())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]

cam = [[-1],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

chk = [[False]*m for _ in range(n)]
result = 10**6

def dfs(y,x,tmp):
    if y == n-1 and x == m-1:
        tmpResult = 0
        for j in range(n):
            for i in range(m):
                if tmp[j][i] == -1:
                    tmpResult += 1
        result = min(result,tmpResult)
    
    for j in range(n):
        for i in range(m):
            if 0<tmp[j][i]<6 and chk[j][i] == False:
                for direc in cam[tmp[j][i]]:
                    tmpCreate = copy.deepcopy(tmp)
                    chk[j][i] = True
                    for di in direc:
                        alpha = 1
                        while True:
                            ny,nx = (j+alpha*dx[di],i+alpha*dy[di])
                            if 0<=ny<n and 0<=nx<m:
                                if tmpCreate[ny][nx] == 0:
                                    tmpCreate[ny][nx] = -1
                                    alpha += 1
                                else:
                                    break
                            else:
                                break
                    dfs(j,i,tmpCreate)
                    chk[j][i] = False


dfs(0,0,maps)

print(result)
import sys
from collections import deque

input = sys.stdin.readline

r,c = map(int,input().rstrip().split())

map = [list(input().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

answer = sys.maxsize
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    global answer
    queue = deque()
    queue.append([y,x,1])
    pfire = 1;
    
    while queue:
        y,x,nfire = queue.popleft()
        # print(y,x,nfire)
        if x == 0 or x == c-1 or y == 0 or y == r-1:
            answer = nfire
        
        if pfire != nfire:
            spreadFire()
            pfire += 1
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<c and 0<= ny<r and map[ny][nx] == '.' and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append([ny,nx,nfire+1])
                
def spreadFire():
    fire = []
    
    for j in range(r):
        for i in range(c):
            if map[j][i] == 'F':
                fire.append([j,i])
                
    for fireY,fireX in fire:
        for d in range(4):
            nfireY = fireY + dy[d]
            nfireX = fireX + dx[d]
            if 0<=nfireX<c and 0<=nfireY<r and map[nfireY][nfireX] != '#':
                map[nfireY][nfireX] = 'F'

for j in range(r):
    for i in range(c):
        if map[j][i] == 'J':
            visited[j][i] = True
            bfs(j,i)
            break

if answer == sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(answer)


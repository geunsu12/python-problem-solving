import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

inputMap = []

for _ in range(n):
    inputMap.append(list(map(int,input().rstrip().split())))

distMap = [[0]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def findDistance(x,y):
    queue = deque()
    queue.append([x,y,0])
    distMap[y][x] = 0
    while queue:
        x,y,dist = queue.popleft()
    
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<m and 0<=ny<n:
                if distMap[ny][nx] == 0 and inputMap[ny][nx] == 1:
                    distMap[ny][nx] = dist+1
                    queue.append([nx,ny,dist+1])
                    
for j in range(n):
    for i in range(m):
        if inputMap[j][i] == 2:
            findDistance(i,j)

for j in range(n):
    for i in range(m):
        if inputMap[j][i] == 1 and distMap[j][i] == 0:
            distMap[j][i] = -1

for row in distMap:
    row = list(map(str,row))
    print(' '.join(row))

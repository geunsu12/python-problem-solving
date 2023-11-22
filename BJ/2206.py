import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

maps = []
visited = [[[0,0] for _ in range(M)] for _ in range(N)]

for i in range(N):
    maps.append(list(map(int,list(input().rstrip()))))

isbreak = 1

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def bfs():
    global visited
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1
    while queue:
        y,x,breakIdx = queue.popleft()
        if (x,y) == (M-1,N-1):
            return visited[y][x][breakIdx]
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<M and 0<=n_y<N:
                if maps[n_y][n_x] == 0 and visited[n_y][n_x][breakIdx] == 0:
                    visited[n_y][n_x][breakIdx] = visited[y][x][breakIdx] + 1
                    queue.append([n_y,n_x,breakIdx])
                elif maps[n_y][n_x] == 1 and visited[n_y][n_x][breakIdx] == 0:
                    if breakIdx == 0:
                        visited[n_y][n_x][1] = visited[y][x][breakIdx] + 1
                        queue.append([n_y,n_x,1])
                    else:
                        continue
    return -1

print(bfs())

                
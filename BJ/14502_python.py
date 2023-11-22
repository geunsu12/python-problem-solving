from itertools import combinations
from collections import deque
import copy
import sys

input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

maps = []
for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))

maxv = -1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    global maxv
    global copymaps

    queue = deque()

    for j in range(n):
        for i in range(m):
            if copymaps[j][i] == 2:
                queue.append([i,j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if copymaps[ny][nx] == 0:
                    copymaps[ny][nx] = 2
                    queue.append([nx,ny])
    tmp = 0 
    for j in range(n):
        for i in range(m):
            if copymaps[j][i] == 0:
                tmp += 1
    maxv = max(maxv,tmp)

empty_list = []

for j in range(n):
    for i in range(m):
        if maps[j][i] == 0:
            empty_list.append([i,j])

for wall_com in combinations(empty_list,3):
    copymaps = copy.deepcopy(maps)
    for wallx, wally in wall_com:
        copymaps[wally][wallx] = 1
    bfs()

print(maxv)
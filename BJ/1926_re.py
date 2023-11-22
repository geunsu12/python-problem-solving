"""
1. 알고리즘
 - 모든 점에 대해서 이동하면서 map[j][i] == 1 and chk[j][i] == False이면 BFS
2. 시간복잡도

O(V+E) = O(V+4V) = O(5V) = 5 * 250000 = 1250000
3. 자료구조
map = int[][]
chk = int[][]
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]

maxv = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    size = 1
    while queue:
        y,x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    size += 1
                    queue.append((ny,nx))
    return size
rs = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            rs += 1
            maxv = max(bfs(j,i),maxv)

print(rs)
print(maxv)
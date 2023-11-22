# PyPy3로는 통과 가능하나, Python3로는 시간초과난다.
# PyPy는 JIT 컴파일을 도입해 CPython보다 빠르다.
# PyPy는 자주 쓰이는 코드를 캐싱하는 기능이 있기 때문에 메모리를 조금 더 사용하면서,속도를 개선했고
# 결과적으로 반복문이 많이 사용되는 코드에선 PyPy가 우세하며,
# 간단한 코드에서는 Python3가 메모리 및 속도 면에서 우세하다.

from collections import deque
import copy

n, m = map(int,input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int,input().split())))

maxv = -1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    global maxv
    queue = deque()
    copymaps = copy.deepcopy(maps)

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

def dfs(wall):
    if wall == 3:
        bfs()
        return
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0:
                maps[y][x] = 1
                dfs(wall+1)
                maps[y][x] = 0
dfs(0)
print(maxv)
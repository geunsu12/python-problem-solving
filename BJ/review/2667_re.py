'''
1. 알고리즘
 - 
2. 시간복잡도
3. 자료구조
'''

import sys

input = sys.stdin.readline

N = int(input())

map = [list(map(int, input().rstrip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]

sizelist = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

size = 0
def DFS(y,x):
    global size
    size += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                DFS(ny,nx)
    return size


for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            size = 0
            sizelist.append(DFS(j,i))

sizelist.sort()
print(len(sizelist))
for i in sizelist:
    print(i)
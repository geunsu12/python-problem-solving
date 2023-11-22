"""
1. 알고리즘
 - map[j][i] == 1 and chk[j][i] == False인 구간에서 DFS돌린다.
 - 크기를 리스트에 넣는다.
2. 시간 복잡도
 - O(V+E) : V+4V = 5V = 5 * 625
3. 자료구조
 - map : int[j][i]
 - chk : int[j][i]

"""

import sys

input = sys.stdin.readline

N = int(input())

map = [list(map(int,input().strip())) for _ in range(N)]

chk = [[False]*N for _ in range(N)]

paint = []

size = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

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
            size = 0
            chk[j][i] = True
            paint.append(DFS(j,i))

print(len(paint))

paint.sort()

for i in paint:
    print(i)

# print(map)

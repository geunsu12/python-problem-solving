import sys
from collections import deque

input = sys.stdin.readline

r,c = map(int,input().split())

maps = []

fireQ = deque()
hunQ = deque()

INF = sys.maxsize

fireDepth = [[INF]*c for _ in range(r)]
hunVisit = [[False]*c for _ in range(r)]

for j in range(r):
    tmp_map = list(input().rstrip())
    for i in range(c):
        if tmp_map[i] == 'F':
            fireQ.append([j,i,0])
            fireDepth[j][i] = 0
        if tmp_map[i] == 'J':
            hunQ.append([j,i,0])
            hunVisit[j][i] = True
    maps.append(tmp_map)

dy = [0,1,0,-1]
dx = [1,0,-1,0]


def fireBFS():
    global maps
    global fireQ
    global fireDepth
    
    while fireQ:
        now_y, now_x, depth = fireQ.popleft()
        # print(now_y, now_x, depth)
        for d in range(4):
            new_y, new_x = (now_y+dy[d],now_x+dx[d])
            if 0<=new_y<r and 0<=new_x<c:
                if fireDepth[new_y][new_x] == INF and maps[new_y][new_x] != '#':
                    fireDepth[new_y][new_x] = depth+1
                    fireQ.append([new_y,new_x,depth+1])
    
def hunBFS():
    global result
    global hunQ
    global hunVisit
    
    while hunQ:
        now_y,now_x,depth = hunQ.popleft()
        if now_y == 0 or now_y == r-1 or now_x == 0 or now_x == c-1:
            # print(now_y,now_x)
            print(depth+1)
            return
        for d in range(4):
            new_y,new_x = (now_y+dy[d],now_x+dx[d])
            if 0<=new_y<r and 0<=new_x<c:
                if maps[new_y][new_x] == '.' and hunVisit[new_y][new_x] == False and depth+1 < fireDepth[new_y][new_x]:
                    hunVisit[new_y][new_x] = True
                    hunQ.append([new_y,new_x,depth+1])
        
    print("IMPOSSIBLE")

fireBFS()
# for j in range(r):
#     print(fireDepth[j])
hunBFS()
from collections import deque


# N, M = map(int,input().split(' '))
# iceM = []
# for i in range(N):
#     iceM.append(list(map(int,input().split(' '))))

N,M = 5, 7
iceM = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0],
        [0, 10, 5, 5, 10, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[False]*M for _ in range(N)]

def iceBreaking(iceM):
    breaking = [[0]*M for _ in range(N)]
    isMelt = False
    for y in range(N):
        for x in range(M):
            if iceM[y][x] != 0:
                isMelt = True
                count = 0
                for d in range(4):
                    new_x = x+dx[d]
                    new_y = y+dy[d]
                    if 0<=new_x<M and 0<=new_y<N:
                        if iceM[new_y][new_x] == 0:
                            count += 1
                breaking[y][x] = count
    if isMelt == False:
        return 0
    
    for y in range(N):
        for x in range(M):
            iceM[y][x] -= breaking[y][x]
            if iceM[y][x] < 0:
                iceM[y][x] = 0
    return 1

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
        
            if 0<=new_x<M and 0<=new_y<N:
                if iceM[new_y][new_x] != 0 and visited[new_y][new_x] == False:
                    visited[new_y][new_x] = True
                    queue.append([new_x,new_y])

years = 0
while True:
    years += 1
    ice = 0
    visited = [[False]*M for _ in range(N)]

    if iceBreaking(iceM) == False:
        print(0)
        break
    print(years)
    for i in range(N):
        print(iceM[i])
    
    for y in range(N):
        for x in range(M):
            if iceM[y][x] !=0 and visited[y][x] == False:
                ice+=1
                bfs(x,y)

    if ice >= 2:
        print(years)
        break
    
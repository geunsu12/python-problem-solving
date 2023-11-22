from collections import deque

def solution(m,n,h):
    tomato = [[] for _ in range(h)]
    for j in range(h):
        for i in range(n):
            tomato[j].append(list(map(int,input().split(' '))))

    dx = [0,1,0,-1,0,0]
    dy = [1,0,-1,0,0,0]
    dz = [0,0,0,0,1,-1]

    update_list = []
    day = -1
    queue = deque()

    def count_zero():
        count = 0
        for k in range(len(tomato)):
            for j in range(len(tomato[0])):
                for i in range(len(tomato[0][0])):
                    if tomato[k][j][i] == 1:
                        queue.append([k,j,i])
    
    def bfs():
        while queue:
            z,y,x = queue.popleft()
            for i in range(6):
                new_x = x+dx[i]
                new_y = y+dy[i]
                new_z = z+dz[i]
                if 0<=new_x<m and 0<=new_y<n and 0<=new_z<h:
                    if tomato[new_z][new_y][new_x] == 0:
                        tomato[new_z][new_y][new_x] = tomato[z][y][x] + 1
                        queue.append([new_z,new_y,new_x])
    max_day = 0
    
    count_zero()
    bfs()

    for k in tomato:
        for j in k:
            if 0 in j:
                print(-1)
                return
            max_day = max(max_day,max(j))
    
    
    print(max_day-1)
m,n,h = map(int,input().split(' '))
solution(m,n,h)
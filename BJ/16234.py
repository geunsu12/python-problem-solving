from collections import deque

n,l,r = map(int,input().split())

pop = []
for j in range(n):
    pop.append(list(map(int,input().split())))

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def bfs(y,x):
    union = [[y,x]]
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True
    
    while queue:
        p_y, p_x = queue.popleft()
        
        for i in range(4):
            n_y = p_y + dy[i]
            n_x = p_x + dx[i]
            if 0<=n_x<n and 0<=n_y<n and visited[n_y][n_x] == False:
                if l<=abs(pop[p_y][p_x]-pop[n_y][n_x])<=r:
                    visited[n_y][n_x] = True
                    union.append([n_y,n_x])
                    queue.append([n_y,n_x])
    if len(union) != 1:
        today_union.append(union)

for day in range(2000):
    visited = [[False]*n for _ in range(n)]
    today_union = []
    for j in range(n):
        for i in range(n):
            if visited[j][i] == False:
                bfs(j,i)

    for union in today_union:
        union_pop = 0
        for uni in union:
            union_pop += pop[uni[0]][uni[1]]
        union_target = int(union_pop/len(union))

        for uni in union:
            pop[uni[0]][uni[1]] = union_target
    if len(today_union) == 0:
        print(day)
        break
    
from collections import deque

N = int(input())

rain = []
for i in range(N):
    rain.append(list(map(int,input().split(' '))))

# N = 7
# rain = [[9, 9, 9, 9, 9, 9, 9],
#         [9, 2, 1, 2, 1, 2, 9],
#         [9, 1, 8, 7, 8, 1, 9],
#         [9, 2, 7, 9, 7, 2, 9],
#         [9, 1, 8, 7, 8, 1, 9],
#         [9, 2, 1, 2, 1, 2, 9],
#         [9, 9, 9, 9, 9, 9, 9]]

# N = 5
# rain = [[6, 8, 2, 6, 2],
#         [3, 2, 3, 4, 6],
#         [6, 7, 3, 3, 2],
#         [7, 2, 5, 3, 6],
#         [8, 9, 5, 2, 7]]

minv = 999
maxv = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]


for j in rain:
    minv = min(minv,min(j))
    maxv = max(maxv,max(j))

# def dfs(x,y):
#     for k in range(4):
#         new_x = x+dx[k]
#         new_y = y+dy[k]
#         if 0<=new_x<N and 0<=new_y<N:
#             if visited[new_y][new_x] == False and rain[new_y][new_x] > h:
#                 visited[new_y][new_x] = True
#                 dfs(new_x,new_y)

def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            new_x = x+dx[k]
            new_y = y+dy[k]
            if 0<=new_x<N and 0<=new_y<N:
                if visited[new_y][new_x] == False and rain[new_y][new_x] > h:
                    visited[new_y][new_x] = True
                    queue.append([new_x,new_y])
max_count = 0

for h in range(0,maxv):
    count = 0
    visited = [[False]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if rain[j][i] > h and visited[j][i] == False:
                visited[j][i] = True
                count += 1
                bfs(i,j)
    max_count = max(max_count,count)

print(max_count)
from collections import deque
def solution(N,M):
    graph = []
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        graph.append(list(map(int,list(input()))))
    
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    def bfs():
        queue = deque()
        queue.append([0,0,1])
        while True:
            x,y,depth = queue.popleft()
            if x == M-1 and y == N-1:
                print(depth)
                return
            for i in range(4):
                n_x = x+dx[i]
                n_y = y+dy[i]
                if 0<=n_x<M and 0<=n_y<N:
                    if visited[n_y][n_x] == False and graph[n_y][n_x] == 1:
                        visited[n_y][n_x] = True
                        queue.append([n_x,n_y,depth+1])
    bfs()

N,M = map(int,input().split())
solution(N,M)
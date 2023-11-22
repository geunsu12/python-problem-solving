from collections import deque

F,S,G,U,D = map(int,input().split())

count = [0 for _ in range(F+1)]
visited = [False]*(F+1)

def bfs(S):
    queue = deque()
    queue.append(S)
    visited[S] = True
    while queue:
        p_floor = queue.popleft()
        if p_floor == G:
            print(count[G])
            return
        down_floor = p_floor-D
        up_floor = p_floor+U
        if down_floor >= 1 and visited[down_floor] == False:
            visited[down_floor] = True
            count[down_floor] = count[p_floor]+1
            queue.append(down_floor)
            
        if up_floor <= F and visited[up_floor] == False:
            visited[up_floor] = True
            count[up_floor] = count[p_floor]+1
            queue.append(up_floor)
    print("use the stairs")

bfs(S)
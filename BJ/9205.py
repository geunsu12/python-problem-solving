from collections import deque
def solution():

    n = int(input())
    c_coordi = []

    h_x, h_y = map(int,input().split(' '))

    for i in range(n):
        c_coordi.append(list(map(int,input().split(' '))))
    r_x, r_y = map(int,input().split(' '))

    visited = [False]*n
    
    def bfs(x,y):
        queue = deque()
        queue.append([x,y])
        while queue:
            p_x, p_y = queue.popleft()

            if abs(r_y-p_y)+ abs(r_x-p_x) <= 1000:
                print("happy")
                return 0
            
            for i in range(n):
                if visited[i] == False:
                    n_x, n_y = c_coordi[i]
                    if abs(n_x-p_x)+abs(n_y-p_y) <= 1000:
                        visited[i] = True
                        queue.append([n_x,n_y])
        print("sad")
    bfs(h_x,h_y)

t = int(input())
for i in range(t):
    solution()
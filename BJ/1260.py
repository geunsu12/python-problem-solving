from collections import deque

def solution(N,M,V):
    graph = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    answer = [V]
    for i in range(M):
        first, second = map(int,input().split(' '))
        graph[first].append(second)
        graph[second].append(first)

    for line in graph:
        line.sort()

    #DFS
    def dfs(start):
        for end in graph[start]:
            if visited[end] == False:
                visited[end] = True
                answer.append(end)
                dfs(end)
        return 0
    
    visited[V] = True
    dfs(V)
    print(' '.join(list(map(str,answer))))

    #BFS
    visited = [False]*(N+1)
    answer = []

    def bfs(start):
        queue = deque()
        queue.append(start)
        while queue:
            p_node = queue.popleft()
            answer.append(p_node)
            for n_node in graph[p_node]:
                if visited[n_node] == False:
                    visited[n_node] = True
                    queue.append(n_node)
    visited[V] = True
    bfs(V)
    print(' '.join(list(map(str,answer))))

N,M,V = map(int, input().split(' '))

solution(N,M,V)

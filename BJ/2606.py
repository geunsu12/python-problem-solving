node = int(input())
line = int(input())

def solution(node, line):
    graph = [[] for _ in range(node+1)]
    for i in range(line):
        first, secon = map(int,input().split())
        graph[first].append(secon)
        graph[secon].append(first)

    visited = [False]*(node+1)
    
    def dfs(p_node):
        visited[p_node] = True
        for n_node in graph[p_node]:
            if visited[n_node] == False:
                dfs(n_node)
    
    dfs(1)
    # print(visited)
    print(sum(visited)-1)

solution(node,line)
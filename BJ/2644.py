def solution(n,target_x,target_y,m):
    graph = [[] for _ in range(n)]
    visited = [False]*m
    for i in range(m):
        st, end = map(int,input().split())
        graph[st].append(end)
        graph[end].append(st)

    answer = 0
    def dfs(p_node, depth):
        nonlocal answer
        if p_node == target_y:
            answer = depth
        
        for n_node in graph[p_node]:
            if visited[n_node] == False:
                visited[n_node] = True
                dfs(n_node,depth+1)
                visited[n_node] = False

    visited[target_x] = True
    dfs(target_x,0)
    
    print(answer)
    
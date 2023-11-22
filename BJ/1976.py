from collections import deque

n = int(input())
m = int(input())

maps = [[0]*(n+1)]

for j in range(n):
    maps.append([0]+list(map(int,input().split())))

cities = list(map(int,input().split()))

def bfs(fromCity,toCity):
    global result

    visit = [False]*(n+1)
    
    queue = deque()
    queue.append(fromCity)
    visit[fromCity] = True

    while queue:
        nowCity = queue.popleft()
        if nowCity == toCity:
            result = True
            return
        for i in range(1,n+1):
            if visit[i] == False and maps[nowCity][i] == 1:
                visit[i] =True
                queue.append(i)

for i in range(m-1):
    result = False
    bfs(cities[i],cities[i+1])
    if result == False:
        break

if result == True:
    print("YES")
else:
    print("NO")
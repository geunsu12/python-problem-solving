from collections import deque

n, k = map(int,input().split())

queue = deque()

visited = [-1]*100001

queue.append(n)
visited[n] = 0

while queue:
    nowNum = queue.popleft()
    if nowNum == k:
        print(visited[nowNum])
        break
    
    if 0<=2*nowNum<100001 and visited[2*nowNum] == -1:
        visited[2*nowNum] = visited[nowNum]
        queue.appendleft(2*nowNum)
        
    if 0<=nowNum-1<100001 and visited[nowNum-1] == -1:
        visited[nowNum-1] = visited[nowNum]+1
        queue.append(nowNum-1)
        
    if 0<=nowNum+1<100001 and visited[nowNum+1] == -1:
        visited[nowNum+1] = visited[nowNum]+1
        queue.append(nowNum+1)

visited = [False]*100001

queue.append([n,0])
visited[n] = True

while queue:
    nowNum, nowSec = queue.popleft()
    if nowNum == k:
        print(nowSec)
        break
    if 0<=2*nowNum<100001 and visited[2*nowNum] == False:
        visited[2*nowNum] = True
        queue.appendleft([2*nowNum,nowSec])
    if 0<=nowNum+1<100001 and visited[nowNum+1] == False:
        visited[nowNum+1] = True
        queue.append([nowNum+1,nowSec+1])
    if 0<=nowNum-1<100001 and visited[nowNum-1] == False:
        visited[nowNum-1] = True
        queue.append([nowNum-1,nowSec+1])

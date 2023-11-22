import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

space = []

for j in range(N):
    space.append(list(map(int,input().rstrip().split())))

fishes = []

for j in range(N):
    for i in range(N):
        if space[j][i] == 9:
            baby = [i,j,2,0]
            space[j][i] = 0
            break

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def findSmallFish(x,y):
    global baby, space
    queue = deque()
    queue.append([x,y,0])
    fishList = []
    chk = [[False]*N for _ in range(N)]
    minDist = 99999
    while(queue):
        p_x, p_y, sec = queue.popleft()
        
        if minDist != 99999 and sec > minDist:
            return sorted(fishList,key = lambda x:(x[1],x[0]))
        
        if 0<space[p_y][p_x]<baby[2]:
            minDist = sec
            fishList.append([p_x,p_y,sec])
        
        for i in range(4):
            n_x = p_x + dx[i]
            n_y = p_y + dy[i]
            if 0<=n_x<N and 0<=n_y<N:
                if chk[n_y][n_x] == False and space[n_y][n_x] <= baby[2]:
                    chk[n_y][n_x] = True
                    queue.append([n_x,n_y,sec+1])
    return fishList
    
result = 0

while True:
    smallFish = findSmallFish(baby[0],baby[1])
    if len(smallFish) == 0:
        print(result)
        break
    smallFish = smallFish[0]
    result += smallFish[2]
    baby = [smallFish[0],smallFish[1],baby[2],baby[3]+1]
    space[smallFish[1]][smallFish[0]] = 0
    if baby[3] == baby[2]:
        baby[2] += 1
        baby[3] = 0
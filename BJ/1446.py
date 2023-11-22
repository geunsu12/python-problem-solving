n,d = map(int,input().split())

road = []
for _ in range(n):
    road.append(list(map(int,input().split())))

road.sort(key = lambda x:x[0])

minv = 9999999

def dfs(y,driveLen):
    global minv
    print(y,driveLen)
    if y >= road[-1][1] and :
        minv = min(minv,driveLen)
        return 0
    for i in range(len(road)):
        if road[i][0] >= y and road[i][1] <=d:
            ny = road[i][1]
            dfs(ny,driveLen+road[i][2]+road[i][])

dfs(0,0)

print(minv)
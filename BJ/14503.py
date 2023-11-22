import sys
input = sys.stdin.readline

# n = 높이, m = 가로
n,m = map(int,input().rstrip().split())

maps = []

r,c,d = map(int, input().rstrip().split())

for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))

dy = [-1,0,1,0]
dx = [0,1,0,-1]

clean = 0

def robot(x,y,d):
    global clean
    
    if maps[y][x] == 0:
        maps[y][x] = 2
        clean += 1
    
    isDirty = False
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 0:
            isDirty = True
            break
    if isDirty == False:
        ny = y-dy[d]
        nx = x-dx[d]
        if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
            return
        else:
            robot(nx,ny,d)
    else:
        d = (d-1)%4
        ny = y+dy[d]
        nx = x+dx[d]
        if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 0:
            robot(nx,ny,d)
        else:
            robot(x,y,d)

robot(c,r,d)
print(clean)
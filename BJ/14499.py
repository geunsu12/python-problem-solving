import sys
input = sys.stdin.readline

n,m,y,x,k = map(int,input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))

rollList = list(map(int,input().rstrip().split()))

dice = [0,0,0,0,0,0]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def roll_dice(roll,x,y):
    global dice
    a,b,c,d,e,f = dice
    # print("in",roll,x,y,dice)
    if roll == 1:
        dice = [d,b,a,f,e,c]
    if roll == 2:
        dice = [c,b,f,a,e,d]
    if roll == 3:
        dice = [e,a,c,d,f,b]
    if roll == 4:
        dice = [b,f,c,d,a,e]

    if maps[y][x] == 0:
        maps[y][x] = dice[-1]
    else:
        dice[-1] = maps[y][x]
        maps[y][x] = 0
    # print("out",roll,x,y,dice)

for roll in rollList:
    n_y = y + dy[roll-1]
    n_x = x + dx[roll-1]
    if 0<=n_x<m and 0<=n_y<n:
        roll_dice(roll,n_x,n_y)
        x,y = n_x,n_y
        print(dice[0])
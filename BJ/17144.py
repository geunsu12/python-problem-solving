import sys
input = sys.stdin.readline

r,c,t = map(int,input().rstrip().split())

house = []
for i in range(r):
    house.append(list(map(int,input().rstrip().split())))
    
for j in range(r):
    if house[j][0] == -1:
        upside = j
        downside = j+1
        break
sec = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]  

def spreadMungi():
    global house,r,c
    tmpHouse = [[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if house[y][x] > 0:
                tmp = 0
                for i in range(4):
                    n_x = x+dx[i]
                    n_y = y+dy[i]
                    if 0<=n_x<c and 0<=n_y<r and house[n_y][n_x] != -1:
                        tmpHouse[n_y][n_x] += house[y][x]//5
                        tmp += house[y][x]//5
                house[y][x] -= tmp

    for j in range(r):
        for i in range(c):
            house[j][i] += tmpHouse[j][i]

def cleanMungi():
    global house, upside, downside

    for i in range(upside-1,0,-1):
        house[i][0] = house[i-1][0]
    for i in range(c-1):
        house[0][i] = house[0][i+1]
    for i in range(0,upside):
        house[i][-1] = house[i+1][-1]
    for i in range(c-1,1,-1):
        house[upside][i] = house[upside][i-1]
    house[upside][1] = 0
    
    for i in range(downside+1,r-1):
        house[i][0] = house[i+1][0]
    for i in range(c-1):
        house[-1][i] = house[-1][i+1]
    for i in range(r-1,downside,-1):
        house[i][-1] = house[i-1][-1]
    for i in range(c-1,1,-1):
        house[downside][i] = house[downside][i-1]
    house[downside][1] = 0
    
while sec < t:
    sec += 1
    spreadMungi()
    # print("spread")
    # for j in range(r):
    #     print(house[j])
    cleanMungi()
    # print("clean")
    # for j in range(r):
    #     print(house[j])
    
result = 0
for j in range(r):
    for i in range(c):
        if house[j][i] > 0:
            result += house[j][i]
            
print(result)
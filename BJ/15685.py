import sys
sys.setrecursionlimit(10**6)

n = int(input())

curves = []

maps = [[0]*101 for _ in range(101)]

for i in range(n):
    curves.append(list(map(int,input().split())))

def makeGen(depth, gen, d):
    global line
    if depth == gen+1:
        return 0
    if depth == 0:
        line.append([line[0][0]+dx[d],line[0][1]+dy[d]])
        makeGen(depth+1, gen, d)
        
    else:
        l = len(line)
        for k in range(l-1,0,-1):
            x,y = line[-1]
            di = [line[k][0]-line[k-1][0],line[k][1]-line[k-1][1]]
            for i in range(4):
                if dx[i] == di[0] and dy[i] == di[1]:
                    ni = (i+1)%4
                    # print(k,x,y,i,ni)
                    nx = x+dx[ni]
                    ny = y+dy[ni]
                    if 0<=nx<=100 and 0<=ny<= 100:
                        line.append([nx,ny])
            
        makeGen(depth+1, gen, d)
                
        
            
dx = [1,0,-1,0]    
dy = [0,-1,0,1]

for curve in curves:
    x,y,d,g = curve
    line = [[x,y]]
    makeGen(0, g, d)
    # print(line)
    
    for l in line:
        maps[l[1]][l[0]] = 1
    

# for m in maps:
#     print(m)
result = 0

for y in range(100):
    for x in range(100):
        if maps[y][x] == 1 and maps[y+1][x] == 1 and maps[y][x+1] == 1 and maps[y+1][x+1] == 1:
            result += 1

print(result)

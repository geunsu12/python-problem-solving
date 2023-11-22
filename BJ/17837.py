import sys

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

chess = [[0]*(n+1)]

for i in range(n):
    chess.append([0]+list(map(int,input().rstrip().split())))
arr = [[[] for _ in range(n+1)] for _ in range(n+1)]
horse = [[] for _ in range(k+1)]

dy = [0,0,-1,1]
dx = [1,-1,0,0]

for i in range(1,k+1):
    y,x,d = map(int,input().rstrip().split())
    horse[i] = [y,x,d-1]
    arr[y][x] += [i]

print(chess)
print(arr)
print(horse)

t = 0

def goForward(y,x,d,mal):
    global n
    ny,nx = y+dy[d], x+dx[d]

    for idx in range(len(arr[y][x])):
        if arr[y][x][idx] == mal:
            tmp_arr = arr[y][x][idx:]
            front_arr = arr[y][x][:idx]
            break

    if 1<=nx<=n and 1<=ny<=n:
        if chess[ny][nx] == 0:
            for hor in tmp_arr:
                horse[hor][:2] = [ny,nx]
            arr[ny][nx] += tmp_arr
            arr[y][x] = front_arr

        if chess[ny][nx] == 1:
            for hor in tmp_arr:
                horse[hor][:2] = [ny,nx]
            arr[ny][nx] += reversed(tmp_arr)
            arr[y][x] = front_arr

        if chess[ny][nx] == 2:
            tmpy, tmpx = y-dy[d], x-dx[d]
            if 1>tmpx or n<tmpx or 1>tmpy or tmpy>n or chess[tmpy][tmpx] == 2:
                horse[mal] = [y,x,(d+2)%4]
                return
            else:
                goForward(y,x,(d+2)%4,mal)
    else:
        tmpy, tmpx = y-dy[d], x-dx[d]
        if tmpx<1 or tmpx>n or tmpy<1 or tmpy>n or chess[tmpy][tmpx] == 2:
            horse[mal] = [y,x,(d+2)%4]
            return
        else:
            if d==0 or d==2:
                d += 1
            else:
                d -= 1
            goForward(y,x,d,mal)
def play():
    t = 0
    while True:
        if t > 1000:
            print(-1)
            return
        for j in range(1,n+1):
            for i in range(1,n+1):
                if len(arr[j][i]) >= 4:
                    print(t)
                    return
        for i in range(1,k+1):
            y,x,d = horse[i]
            goForward(y,x,d,i)
        t += 1

play()
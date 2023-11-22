n = int(input())

k = int(input())

maps = [[0]*(n+1) for _ in range(n+1)]

# 0초 초기화
snake = [[1,1]] # y, x
direc = 0
ans = 0
leng = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 사과 초기화
for _ in range(k):
    y, x = map(int,input().split())
    maps[y][x] = 1


# 방향 전환 초기화
l = int(input())
play = []

for _ in range(l):
    sec, turn = input().split()
    play.append([int(sec),turn])

while True:
    head = snake[0]
    if play and play[0][0] == ans:
        if play[0][1] == 'D':
            direc = (direc+1)%4
        else:
            direc = (direc-1)%4
        play.pop(0)
    
    n_y = head[0]+dy[direc]
    n_x = head[1]+dx[direc]

    if n_y < 1 or n_y > n or n_x < 1 or n_x > n:
        break
    elif [n_y,n_x] in snake:
        break
    else:
        snake = [[n_y,n_x]] + snake

    if maps[n_y][n_x] == 0:
        snake.pop()
    else:
        maps[n_y][n_x] = 0
    ans += 1

print(ans+1)
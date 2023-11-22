import sys

input = sys.stdin.readline

n,m = map(int,input().split())

maps = []

blocks = [[[0,0],[1,0],[2,0],[3,0]], # 1
          [[0,0],[0,1],[0,2],[0,3]],
          [[0,0],[0,1],[1,0],[1,1]], # 2
          [[0,0],[0,1],[0,2],[1,2]], # 3 ㄴ
          [[0,0],[1,0],[2,0],[2,-1]], # ㄴ 반대
          [[0,0],[1,0],[2,0],[2,1]], # ㄱ
          [[0,0],[1,0],[0,1],[0,2]], # ㄱ 반대
          [[0,0],[0,1],[1,1],[2,1]], #
          [[0,0],[1,0],[1,1],[1,2]], #
          [[0,0],[1,0],[2,0],[0,1]], #
          [[0,0],[0,1],[0,2],[-1,2]], #
          [[0,0],[0,1],[1,1],[1,2]], # 4
          [[0,0],[1,0],[1,-1],[2,-1]],
          [[0,0],[1,0],[1,1],[2,1]],
          [[0,0],[1,0],[1,-1],[0,1]],
          [[0,0],[1,0],[2,0],[1,1]], # 5 ㅜ
          [[0,0],[0,1],[0,2],[-1,1]], # ㅓ
          [[0,0],[1,0],[2,0],[1,-1]], # ㅗ
          [[0,0],[0,1],[0,2],[1,1]] # ㅏ
        ]

def search(x,y):
    global max_num
    
    for block in blocks:
        nx1,ny1 = x+block[0][0],y+block[0][1]
        nx2,ny2 = x+block[1][0],y+block[1][1]
        nx3,ny3 = x+block[2][0],y+block[2][1]
        nx4,ny4 = x+block[3][0],y+block[3][1]

        if 0<=nx1<m and 0<=nx2<m and 0<=nx3<m and 0<=nx4<m and 0<=ny1<n and 0<=ny2<n and 0<=ny3<n and 0<=ny4<n:
            tmp_sum = maps[ny1][nx1]+maps[ny2][nx2]+maps[ny3][nx3]+maps[ny4][nx4]
            max_num = max(max_num,tmp_sum)


for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))
    
max_num = -1    
    
for y in range(n):
    for x in range(m):
        search(x,y)

print(max_num)
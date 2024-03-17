import sys

input = sys.stdin.readline

n, d = map(int, input().split())

shortcut = []
visit = [False]*n

for i in range(n):
    shortcut.append(list(map(int,input().rstrip().split())))

now = 0
minv = 999999

def dfs(now,total):
    global minv
    # print("now : ",now,"total : ",total, "minv : ",minv)
    if now == d:
        minv = min(minv,total)
        return
    for i in range(n):
        if visit[i] == False and shortcut[i][0] >= now and shortcut[i][1] <= d:
            visit[i] = True
            dfs(shortcut[i][1], total + (shortcut[i][0]-now + shortcut[i][2]))         
            visit[i] = False
    minv = min(minv,total+(d-now))

dfs(0,0)
print(minv)
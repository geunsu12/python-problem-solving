import sys
sys.setrecursionlimit(10**5)

imput = sys.stdin.readline

n = int(input())

promise = []

for _ in range(n):
    promise.append(list(map(int,input().rstrip().split())))

max_num = -1
    
def dfs(day,gain):
    global max_num
    if day >= n:
        max_num = max(max_num,gain)
        return
    if day+promise[day][0] <= n:
        dfs(day+promise[day][0],gain+promise[day][1])
    dfs(day+1,gain)
    
dfs(0,0)

print(max_num)
import sys

INF = sys.maxsize

n = int(input())

nums = list(map(int,input().split()))

oprnd = list(map(int,input().split()))

maxv = -INF
minv = INF
def dfs(nowNum,k):
    global maxv
    global minv
    if k == n:
        maxv = max(maxv,nowNum)
        minv = min(minv,nowNum)
        return
    for i in range(4):
        if oprnd[i] > 0:
            if i == 0:
                nextNum = nowNum+nums[k]
            if i == 1:
                nextNum = nowNum-nums[k]
            if i == 2:
                nextNum = nowNum*nums[k]
            if i == 3:
                if nowNum > 0:
                    nextNum = nowNum//nums[k]
                else:
                    nextNum = -((-nowNum) //nums[k])
            oprnd[i] -= 1
            dfs(nextNum,k+1)
            oprnd[i] += 1

dfs(nums[0],1)

print(maxv)
print(minv)
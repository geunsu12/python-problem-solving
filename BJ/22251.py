led = [
    # 0
    [1,1,1,1,1,1,0],
    # 1
    [0,1,1,0,0,0,0],
    # 2
    [1,1,0,1,1,0,1],
    # 3
    [1,1,1,1,0,0,1],
    # 4
    [0,1,1,0,0,1,1],
    # 5
    [1,0,1,1,0,1,1],
    # 6
    [1,0,1,1,1,1,1],
    # 7
    [1,1,1,0,0,0,0],
    # 8
    [1,1,1,1,1,1,1],
    # 9
    [1,1,1,1,0,1,1]
]
ledControl = []

for i in range(10):
    tmp = [0]*10
    for j in range(10):
        tmpN = 0
        for k in range(7):
            if led[i][k] != led[j][k]:
                tmpN += 1
        tmp[j] = tmpN
    ledControl.append(tmp)
# print(ledControl)

n,k,p,x = map(int,input().split())

def dfs(nowNum,depth, remainP):
    # print("dfs",nowNum,depth, remainP)
    global result
    if depth == k:
        if 1<= int(nowNum) <= n:
            result += 1
            # print(nowNum)
        return
    for i in range(10):
        nextP = remainP - ledControl[int(nowNum[depth])][i]
        if nextP >= 0:
            nextNum = nowNum[:depth]+str(i)+nowNum[depth+1:]
            dfs(nextNum,depth+1,nextP)
    

result = 0
x = "0"*(k-len(str(x)))+str(x)

dfs(x,0,p)

print(result-1)
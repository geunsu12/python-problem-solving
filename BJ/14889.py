# Combination 조합을 구할 때 range 범위에 시작 조건을 추가해 그냥 순열과 구분되게 프로그래밍한다.
# 이 문제는 효율성이 중요하므로, 의미없는 연산들은 줄일 수 있도록 한다.
# 

import sys

input = sys.stdin.readline

n = int(input())

status = []
chk = [False]*n

for i in range(n):
    status.append(list(map(int,input().split())))

result = 10**8

def getDiffer():
    global result
    scoreA = 0
    scoreB = 0

    for i in range(n):
        for j in range(n):
            if chk[i] == True and chk[j] == True:
                scoreA += status[i][j]
            elif chk[i] == False and chk[j] == False:
                scoreB += status[i][j]

    result = min(result,abs(scoreA-scoreB))

def dfs(num,st):
    if num == n/2:
        getDiffer()
        return

    for i in range(st,n):
        if chk[i] == False:
            chk[i] = True
            dfs(num+1,i+1)
            chk[i] = False
dfs(0,0)
print(result)
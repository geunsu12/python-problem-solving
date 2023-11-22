import sys

sys.setrecursionlimit(10**5)

s = input()
t = input()
answer = 0

def dfs(nowT):
    global answer
    if len(nowT) < len(s):
        return 0
    if nowT == s:
        answer = 1
        return 0
    
    if nowT[-1] == 'A':
        dfs(nowT[:-1])
    if nowT[0] == 'B':
        tmp = nowT[::-1]
        dfs(tmp[:-1])
        
dfs(t)

print(answer)
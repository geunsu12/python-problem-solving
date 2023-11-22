import sys
input = sys.stdin.readline

n = int(input())

tower = list(map(int,input().rstrip().split()))
ans = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        ans.append(0)
    stack.append([i,tower[i]])
    

print(' '.join(map(str,ans)))

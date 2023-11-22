import sys
import math
input = sys.stdin.readline


N = int(input().rstrip())

buildings = list(map(int,input().rstrip().split()))

stack = []

result = [0]*N
building_result = [-100001]*N

for i in range(N):
    while stack:
        if stack[-1][1] <= buildings[i]:
            stack.pop()
        else:
            break
    result[i] += len(stack)
    if stack:
        building_result[i] = stack[-1][0]+1
    stack.append([i,buildings[i]])

stack = []

for i in range(N-1,-1,-1):
    while stack:
        if stack[-1][1] <= buildings[i]:
            stack.pop()
        else:
            break
    result[i] += len(stack)
    if stack:
        if abs(i - (building_result[i]-1)) > abs(stack[-1][0]-i):
            building_result[i] = stack[-1][0]+1
    stack.append([i,buildings[i]])
    
for i in range(N):
    if result[i] != 0:
        print(result[i],building_result[i])
    else:
        print(result[i])

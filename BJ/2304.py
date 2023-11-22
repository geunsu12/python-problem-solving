import sys

input = sys.stdin.readline

n = int(input())

pillars = [0]*1001

max_height = -1
max_idx = -1

for _ in range(n):
    loc, height = map(int,input().rstrip().split())
    pillars[loc] = height
    if max_height < height:
        max_height = height
        max_idx = loc

curr_pill = 0
result = 0
for i in range(max_idx+1):
    curr_pill = max(pillars[i],curr_pill)
    result += curr_pill

curr_pill = 0
for i in range(1000,max_idx,-1):
    curr_pill = max(curr_pill,pillars[i])
    result += curr_pill
    
print(result)
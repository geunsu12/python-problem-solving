import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

gems = []
bags = []

for i in range(n):
    m,v = map(int,input().rstrip().split())
    gems.append([m,v])

for i in range(k):
    c = int(input())
    bags.append(c)

bags.sort()
gems.sort()
gems = deque(gems)
ans = 0
tmp = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp,-gems[0][1])
        gems.popleft()
    if tmp:
        ans += -heapq.heappop(tmp)

print(ans)

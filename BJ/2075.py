import sys
input = sys.stdin.readline

import heapq

N = int(input())
lists = []

for j in range(N):
    tmp = list(map(int, input().rstrip().split()))
    for t in tmp:
        if len(lists) < N:
            heapq.heappush(lists,t)
        else:
            if lists[0] < t:
                heapq.heappop(lists)
                heapq.heappush(lists,t)

print(lists[0])
import sys
import heapq

input = sys.stdin.readline

V,E = map(int,input().rstrip().split())

INF = sys.maxsize

dist = [INF]*(V+1)
edge = [[] for _ in range(V+1)]

k = int(input().rstrip())

for i in range(E):
    u,v,w = map(int,input().rstrip().split())
    edge[u].append([w,v])

heap = [[0,k]]
dist[k] = 0

while heap:
    pw, pv = heapq.heappop(heap)
    if dist[pv] != pw: continue
    for nw, nv in edge[pv]:
        if dist[nv] > pw + nw:
            dist[nv] = pw + nw
            heapq.heappush(heap,[dist[nv],nv])

for i in range(1,V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
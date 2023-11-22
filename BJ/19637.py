import sys

input = sys.stdin.readline

N, M = map(int,input().split())

scores = []

for i in range(N):
    tmp = input().split()
    scores.append([int(tmp[1]),tmp[0]])

def bin_search(st,end,target):
    if st==end:
        print(scores[st][1])
        return
    mid = (st+end)//2
    if target > scores[mid][0]:
        bin_search(mid+1,end,target)
    else:
        bin_search(st,mid,target)

for i in range(M):
    bin_search(0,N-1,int(input()))

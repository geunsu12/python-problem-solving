import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())

requests = list(map(int,input().split()))

M = int(input())

def getSumBudget(margin):
    sum = 0
    for req in requests:
        if req < margin:
            sum+=req
        else:
            sum+=margin
    return sum

def bin_search(st,end,budget):
    if st == end:
        if getSumBudget(st) <= budget:
            print(st)
            return
        else:
            print(st-1)
            return
    mid = (st+end)//2
    sum_mid = getSumBudget(mid)
    if sum_mid <= budget:
        bin_search(mid+1,end,budget)
    else:
        bin_search(st,mid,budget)

if sum(requests) <= M:
    print(max(requests))
else:
    bin_search(0,100000,M)
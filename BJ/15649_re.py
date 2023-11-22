import sys
input = sys.stdin.readline

N, M = map(int,input().split())

chk = [False]*(N+1)

rs = []

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return 0
    for i in range(1,N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()

recur(0)
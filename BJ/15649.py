"""

1. 알고리즘
 - 백트래킹을 해서 순열
2. 시간복잡도
 - 시간복잡도 중복 x : O(N!) < 10 가능

3. 자료구조
 -
 
"""

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))        
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()

recur(0)
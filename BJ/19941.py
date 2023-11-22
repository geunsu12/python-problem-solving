import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

lists = list(input().rstrip())

ans = 0

for i in range(N):
    if lists[i] == 'P':
        for j in range(max(0,i-K),min(N,i+K+1)):
            if lists[j] == 'H':
                lists[j] = 0
                ans += 1
                break
print(lists)
print(ans)

# 20 1
# HHPHPPHHPPHPPPHPHPHP 8

# 20 2
# HHHHHPPPPPHPHPHPHHHP 7


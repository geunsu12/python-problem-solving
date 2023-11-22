import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n,m = map(int,input().split())

dp = []
for _ in range(n):
    dp.append(list(map(int,input().rstrip().split())))

dy = [0,1,0]
dx = [1,0,-1]

for i in range(1,m):
    dp[0][i] += dp[0][i-1]

for j in range(1,n):
    left_right = dp[j][:]
    right_left = dp[j][:]

    for i in range(m):
        if i == 0:
            left_right[i] += dp[j-1][i]
        else:
            left_right[i] += max(dp[j-1][i],left_right[i-1])
    
    for i in range(m-1,-1,-1):
        if i == m-1:
            right_left[i] += dp[j-1][i]
        else:
            right_left[i] += max(dp[j-1][i],right_left[i+1])

    for i in range(m):
        dp[j][i] = max(right_left[i],left_right[i])

print(dp[n-1][m-1])
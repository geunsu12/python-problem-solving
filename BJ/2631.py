n = int(input())

lists = []
for i in range(n):
    lists.append(int(input()))

dp = [1]+[0]*(n-1)

for i in range(1,n):
    for j in range(i):
        if lists[j] < lists[i]:
            dp[i] = max(dp[i],dp[j])
    dp[i] += 1

print(n-max(dp))
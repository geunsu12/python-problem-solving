n = int(input())

nums = [0]*(n+1)
visited = [False]*(n+1)
for i in range(1,n+1):
    nums[i] = int(input())

ans = 0
num_ans = []

def dfs(n):
    global ans,num_ans
    if tmp == tmp2:
        ans += len(tmp)
        num_ans += list(tmp)
        return 0
    next = nums[n]
    if visited[next] == False:
        tmp.add(next)
        tmp2.add(nums[next])
        visited[next] = True
        dfs(next)
        visited[next] = False


for i in range(1,n+1):
    if visited[i] == False:
        tmp = set([i])
        tmp2 = set([nums[i]])
        visited[i] = True
        dfs(i)

print(ans)
num_ans.sort()
for num in num_ans:
    print(num)
n = int(input())

people = [0]+list(map(int,input().rstrip().split()))

ans = [0]*n

for i in range(1,n+1):
    target = people[i]
    left = 0
    for j in range(n):
        if ans[j] == 0:
            if left == target:
                ans[j] = i
                break
            else:
                left += 1

print(' '.join(map(str,ans)))
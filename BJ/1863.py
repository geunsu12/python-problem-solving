import sys

input = sys.stdin.readline

n = int(input())

skyline = []
visited = [False]*n

for i in range(n):
    skyline.append(list(map(int,input().rstrip().split())))

ans = 0

for i in range(n):
    if skyline[i][1] > 0 and visited[i] == False:
        start = skyline[i]
        # print("start ",start)
        ans += 1
        for j in range(i+1,n):
            if skyline[j][1] == start[1]:
                visited[j] = True
            if skyline[j][1] < start[1]:
                # print("end ",skyline[j])
                break
print(ans)
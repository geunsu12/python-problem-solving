N = int(input())

plist = []

for i in range(N):
    W, H = map(int(input().split()))
    plist.append([H,W])
    
for i in range(N):
    for j in range(N):
        rank = 0
        if i!=j:
            if plist[i][0] >= plist[j][0] and plist[i][1] >= plist[j][1]:
                rank += 1
        print(rank," ",end=' ')

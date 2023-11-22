import copy

n,m,l,k = map(int,input().split())

stars = []

for i in range(k):
    stars.append(list(map(int,input().split())))
answer = -1

Edges = []

for i in range(k):
    for j in range(k):
        Edges.append([stars[i][0],stars[j][1]])
        Edges.append([stars[j][0],stars[i][1]])

for eachEdge in Edges:
    tmpX,tmpY = eachEdge
    tmpAns = 0
    for eachStar in stars:
        if tmpX <= eachStar[0] <= tmpX+l and tmpY <= eachStar[1] <= tmpY+l:
            tmpAns += 1
    answer = max(answer,tmpAns)

print(k-answer)
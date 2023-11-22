N, K = map(int,input().split())

nation = []
for i in range(N):
    nation.append(list(map(int,input().split(' '))))
    
sort_nation = nation.sort(key = lambda x:(x[1],x[2],x[3]))

prize = 0
target = 0

for i in range(N):
    if nation[i][0] == K:
        target = i
        break

for i in range(N):
    if nation[i] == nation[target]:
        print(i+1)
    break
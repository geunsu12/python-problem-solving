n = int(input())
buildings = [0]+list(map(int,input().split()))
results = [0]*(n+1)

def findBuilding(a,b):
    if buildings[a] > buildings[b]:
        bigIdx = a
    else:
        bigIdx = b
    maxIdx = max(a,b)
    minIdx = min(a,b)
    
    if buildings[a] != buildings[b]:
        angle = (buildings[a]-buildings[b])/(a-b)
    else:
        angle = 0
    bias = buildings[a]-(angle*a)

    for i in range(minIdx+1,maxIdx):
        if angle*i+bias <= buildings[i]:
            return False
    return True
    

for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j:
            result = findBuilding(i,j)
            if result:
                results[i] += 1

print(max(results))
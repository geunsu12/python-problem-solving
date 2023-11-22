import sys
import copy

input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

city = []

for _ in range(n):
    city.append(list(map(int,input().rstrip().split())))
    
chickList = []
houseList = []

for j in range(n):
    for i in range(n):
        if city[j][i] == 2:
            chickList.append([i,j])
        if city[j][i] == 1:
            houseList.append([i,j])

result = sys.maxsize

def getCombination(list,n):
    tmp = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(list)):
        el = list[i]
        restList = list[i+1:]
        for c in getCombination(restList,n-1):
            tmp.append([el]+c)
    return tmp

def getChickDist(chickList):
    chickdist = 0
    for house in houseList:
        tmpMin = 99999
        for chick in chickList:
            tmpMin = min(tmpMin,(abs(house[0]-chick[0])+abs(house[1]-chick[1])))
        chickdist += tmpMin
    return chickdist
        

for i in range(m+1):
    combList = getCombination(chickList,i)
    for com in combList:
        result = min(result,getChickDist(com))

print(result)
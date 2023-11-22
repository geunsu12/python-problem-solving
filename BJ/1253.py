import sys

input = sys.stdin.readline

n = int(input())

nlist = list(map(int,input().rstrip().split()))
nlist.sort()
answer = 0

def findTwoPointer(target,tmpList):
    left = 0
    right = len(tmpList)-1
    tmpN = len(tmpList)
    while left < right:
        if tmpList[left]+tmpList[right] == target:
            return True
        if tmpList[left]+tmpList[right] < target:
            left += 1
        else:
            right -= 1
    return False


for t in range(n):
    target = nlist[t]
    tmp = nlist[:t] + nlist[t+1:]
    if findTwoPointer(target,tmp):
        answer += 1

print(answer)
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input().rstrip())

nlist = list(map(int,input().rstrip().split()))

nlist.sort()

answer = 0
answer_list = []
def binary_search(st,end,target):
    print(nlist[st],nlist[end],target)
    if st == end:
        if nlist[st] == target:
            return True
        else:
            return False
    mid = (st+end)//2
    
    if nlist[mid] < target:
        return binary_search(mid+1,end,target)
    else:
        return binary_search(st,mid,target)
        
target_n = 2
while target_n < n:
    start = 0
    while start+1 < target_n:
        print("while문",nlist[start],nlist[target_n])
        tmp = binary_search(start+1,target_n-1,nlist[target_n]-nlist[start])
        if tmp == True:
            answer_list.append(nlist[target_n])
            answer += 1
            break
        else:
            start += 1
    target_n += 1

print(answer)
print(answer_list)
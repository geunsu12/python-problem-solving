import sys

input = sys.stdin.readline

n = int(input())

nlist = list(map(int,input().rstrip().split()))

result = 0

tflist = [False]*(100001)

start = 0
end = 0

while start < n and end < n:
    if tflist[nlist[end]] == False:
        tflist[nlist[end]] = True
        end += 1
        result += (end-start)
    else:
        tflist[nlist[start]] = False
        start+= 1

print(result)
        
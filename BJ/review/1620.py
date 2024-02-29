import sys

input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

dictNum = {}
dictString = {}

for i in range(1,n+1):
    poketmon = input().rstrip()
    dictNum[i] = poketmon
    dictString[poketmon] = i


for i in range(m):
    tmp = input().rstrip()
    if(tmp.isalpha()):
        print(dictString[tmp])
    else:
        print(dictNum[int(tmp)])
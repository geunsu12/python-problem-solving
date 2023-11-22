import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

dic = {}

for i in range(N):
    tmp = input().rstrip()
    if len(tmp) < M:
        continue
    else:
        if tmp not in dic:
            dic[tmp] = 1
        else:
            dic[tmp] += 1

answer = sorted(dic.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))

for i in range(len(answer)):
    print(answer[i][0])
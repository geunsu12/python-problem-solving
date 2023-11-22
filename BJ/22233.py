import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

dic = dict()

for _ in range(N):
    dic[input().rstrip()] = 1

total = len(dic.keys())

for _ in range(M):
    tmp = list(input().rstrip().split(','))
    for word in tmp:
        if word in dic.keys() and dic[word] == 1:
            dic[word] -= 1
            total -= 1
    print(total)
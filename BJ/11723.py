import sys

input = sys.stdin.readline

iter = int(input())
S = set()

for i in range(iter):
    tmp = input().rstrip().split(' ')
    print(tmp)

    if len(tmp) == 2:
        tmp[1] = int(tmp[1])
        if tmp[0] == 'add':
            S.add(tmp[1])
        if tmp[0] == 'remove':
            S.discard(tmp[1])
        if tmp[0] == 'check':
            isCheck = 1 if tmp[1] in S else 0
            print(isCheck)
        if tmp[0] == 'toggle':
            isCheck = 1 if tmp[1] in S else 0
            if isCheck:
                S.remove(tmp[1])
            else:
                S.add(tmp[1])
    else:
        if tmp[0] == 'all':
            S = set(range(1,21))
        if tmp[0] == 'empty':
            S = set()
    print(S)
    
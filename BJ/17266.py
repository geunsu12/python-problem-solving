N = int(input())
M = int(input())
pill = list(map(int,input().rstrip().split(" ")))
pillH = pill[0]

for i in range(len(pill)):
    if i == len(pill)-1:
        pillH = max(pillH,N-pill[i])
    else:
        if i != 0:
            tmp = pill[i]-pill[i-1]
            if tmp % 2 == 0:
                pillH = max(pillH, tmp//2)
            else:
                pillH = max(pillH, tmp//2+1)
                
print(pillH)
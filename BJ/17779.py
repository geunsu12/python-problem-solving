import sys

input = sys.stdin.readline

n = int(input())
arr = [[0]*(n+1)]

for i in range(n):
    arr.append([0]+list(map(int,input().rstrip().split())))

result = 10000000

total_sum = 0

for i in range(1,n+1):
    total_sum += sum(arr[i])

def getDiff(x,y,d1,d2):
    global n
    global total_sum

    tmp_arr = [[0]*(n+1) for _ in range(n+1)]
    people = [0]*5

    #sec 5 cond.#2
    for i in range(d1+1):
        tmp_arr[x+i][y-i] = 5
    for i in range(d2+1):
        tmp_arr[x+i][y+i] = 5
    for i in range(d2+1):
        tmp_arr[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        tmp_arr[x+d2+i][y+d2-i] = 5

    #sec 1 -> people 0
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if tmp_arr[r][c] == 5:
                break
            people[0] += arr[r][c]
    
    #sec 2 -> people 1
    for r in range(1,x+d2+1):
        for c in range(n,y,-1):
            if tmp_arr[r][c] == 5:
                break
            people[1] += arr[r][c]
    
    #sec 3 -> people 2
    for r in range(x+d1,n+1):
        for c in range(1,y-d1+d2):
            if tmp_arr[r][c] == 5:
                break
            people[2] += arr[r][c]
    
    #sec 4 -> people 3
    for r in range(x+d2+1,n+1):
        for c in range(n,y-d1+d2-1,-1):
            if tmp_arr[r][c] == 5:
                break
            people[3] += arr[r][c]
    
    #sec 5 -> people 4
    people[4] = total_sum-sum(people)

    return (max(people)-min(people))

for y in range(1,n+1):
    for x in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if n < x+d1+d2:
                    continue
                if 1 > y-d1:
                    continue
                if y+d2 > n:
                    continue
                result = min(result,getDiff(x,y,d1,d2))

print(result)
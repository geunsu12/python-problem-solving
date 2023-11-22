n = int(input())
now = list(map(int,list(input())))
target = list(map(int,list(input())))

def getResult():
    now_copy = now[:]
    result = 0
    for i in range(1,n):
        if now_copy[i-1] == target[i-1]:
            continue
        else:
            now_copy[i-1] = 1-now_copy[i-1]
            now_copy[i] = 1-now_copy[i]
            if i != n-1:
                now_copy[i+1] = 1-now_copy[i+1]
            result += 1
    if now_copy == target:
        return result
    else:
        return 10**10

first_case = getResult()

now[0] = 1-now[0]
now[1] = 1-now[1]

second_case = 1+getResult()

result = min(first_case,second_case)

if result == 10**10:
    print(-1)
else:
    print(result)
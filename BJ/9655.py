n = int(input())
answer = [-1]*1001

# 0 => 상근(SK) / 1=> 창영(CY)
answer[1] = 0
answer[2] = 1
answer[3] = 0

for i in range(4,n+1):
    if answer[i-1] == 1:
        answer[i] = 0
    else:
        answer[i] = 1

if answer[n] == 0:
    print("SK")
else:
    print("CY")
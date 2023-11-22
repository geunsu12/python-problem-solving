gears = [list(input()) for i in range(4)]

# print(gears)

k = int(input())

def shiftList(list, shift):
    # print(list)
    if shift == 1:
        list = [list[7]]+list[:7]
    elif shift == -1:
        list = list[1:]+[list[0]]
    return list

for _ in range(k):
    gear, d = map(int,input().split())
    rotate = [0]*4
    rotate[gear-1] = d

    for i in range(1,4):
        if 0<= gear-1+i < 4:
            if gears[gear-1+i][6] != gears[gear-2+i][2]:
                rotate[gear-1+i] = - rotate[gear-2+i]
        if 0<= gear-1-i < 4:
            if gears[gear-1-i][2] != gears[gear-i][6]:
                rotate[gear-1-i] = - rotate[gear-i]
    for i in range(4):
        gears[i] = shiftList(gears[i],rotate[i])

result = 0

for i in range(4):
    result += (2**i)*int(gears[i][0])

print(result)
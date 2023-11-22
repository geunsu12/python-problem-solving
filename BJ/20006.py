import sys
input = sys.stdin.readline
p,m = list(map(int,input().rstrip().split()))

plLev,plNick = input().rstrip().split()

rooms = [[[int(plLev),plNick]]]

for i in range(p-1):
    plLev, plNick = input().rstrip().split()
    isInList = False
    for room in rooms:
        if len(room) < m and abs(int(plLev) - room[0][0]) <= 10:
            room.append([int(plLev), plNick])
            isInList = True
            break
    if isInList == False:
        rooms.append([[int(plLev),plNick]])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key = lambda x:x[1])
    for pl in room:
        print(pl[0],pl[1])
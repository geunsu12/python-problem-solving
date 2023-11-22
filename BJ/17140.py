import sys

input = sys.stdin.readline

r,c,k = map(int, input().rstrip().split())

arr = []

for j in range(3):
    arr.append(list(map(int,input().rstrip().split())))
t = 0

def Rsort():
    global arr
    tmp_arr = []
    for j in range(len(arr)):
        tmp = dict(zip(range(1,101),[0]*101))
        
        for i in range(len(arr[0])):
            if arr[j][i] != 0:
                tmp[arr[j][i]] += 1
        tmp = list(zip(tmp.keys(),tmp.values()))
        tmp.sort(key = lambda x : (x[1],x[0]))
        t = []
        for i in range(100):
            if tmp[i][1] != 0:
                t += tmp[i]
        tmp_arr.append(t)
    max_row = 0
    for i in range(len(tmp_arr)):
        max_row = max(max_row,len(tmp_arr[i]))
    for i in range(len(tmp_arr)):
        tmp_arr[i] += [0]*(max_row-len(tmp_arr[i]))
    arr = tmp_arr

def Csort():
    global arr
    tmp_arr = []
    for i in range(len(arr[0])):
        tmp = dict(zip(range(1,101),[0]*101))
        
        for j in range(len(arr)):
            if arr[j][i] != 0:
                tmp[arr[j][i]] += 1
        tmp = list(zip(tmp.keys(),tmp.values()))
        tmp.sort(key = lambda x : (x[1],x[0]))
        t = []
        for i in range(100):
            if tmp[i][1] != 0:
                t += tmp[i]
        tmp_arr.append(t)
    max_row = 0
    for i in range(len(tmp_arr)):
        max_row = max(max_row,len(tmp_arr[i]))
    for i in range(len(tmp_arr)):
        tmp_arr[i] += [0]*(max_row-len(tmp_arr[i]))
    arr = [[0]*len(tmp_arr) for _ in range(len(tmp_arr[0]))]
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            arr[j][i] = tmp_arr[i][j]

while True:
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        print(t)
        break
    if t > 100:
        print(-1)
        break
        
    t += 1
    if len(arr) >= len(arr[0]):
        # R 연산 행의 개수 >= 열의 개수
        Rsort()
    else:
        # C 연산 행의 개수 < 열의 개수
        Csort()
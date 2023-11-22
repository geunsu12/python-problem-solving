import sys
import copy

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

a = list(map(int,input().rstrip().split()))
robot = [0]*(2*n)

negu = 0

for i in a:
    if i != 0:
        negu += 1

neguZero = 2*n-negu
ans = 0

while neguZero < k:
    a = [a[-1]]+a[:-1]
    robot = [robot[-1]]+robot[:-1]

    if robot[n-1] == 1:
        robot[n-1] = 0

    for i in range(n-1,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and a[i+1] > 0:
            robot[i+1] = 1
            robot[i] = 0
            a[i+1] -= 1
            if a[i+1] == 0:
                neguZero += 1
    if robot[n-1] == 1:
        robot[n-1] = 0

    if a[0] > 0:
        robot[0] += 1
        a[0] -= 1
        if a[0] == 0:
            neguZero += 1
    if robot[n-1] == 1:
        robot[n-1] = 0
    ans += 1

print(ans)
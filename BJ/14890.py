#Non-Self
import sys
input = sys.stdin.readline

n, l = map(int,input().rstrip().split())

maps = []

for _ in range(n):
    maps.append(list(map(int,input().rstrip().split())))

result = 0

def check_line(line):
    slope = [False]*n
    for i in range(1,n):
        if abs(line[i-1] - line[i]) > 1:
            return False
        if line[i-1] > line[i]:
            for j in range(l):
                if i+j >= n or line[i] != line[i+j] or slope[i+j]:
                    return False
                if line[i] == line[i+j]:
                    slope[i+j] = True
        if line[i-1] < line[i]:
            for j in range(l):
                if i-j-1 < 0 or line[i-j-1] != line[i-1] or slope[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    slope[i-j-1] = True
    return True
        
for j in range(n):
    if check_line([maps[j][i] for i in range(n)]):
        result += 1

for i in range(n):
    if check_line([maps[j][i] for j in range(n)]):
        result += 1

print(result)
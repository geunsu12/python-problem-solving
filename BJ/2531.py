import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = []

total = [0]*(d+1)
maxv = -1
types = 0

for _ in range(n):
    sushi.append(int(input()))

sushi = sushi*2

for i in range(k):
    total[sushi[i]] += 1
    
for i in range(d+1):
    if total[i] > 0:
        types += 1
if total[c] == 0:
    types += 1
    
maxv = max(maxv,types)

left = 0
right = k-1

for i in range(n-1):
    total[sushi[left]] -= 1
    if total[sushi[left]] == 0 and sushi[left] != c:
        types -= 1
    
    left += 1
    right += 1
    if sushi[right] != c and total[sushi[right]] == 0:
        types += 1
    total[sushi[right]] += 1
    maxv = max(maxv,types)
    
print(maxv)
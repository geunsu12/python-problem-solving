h, w = map(int,input().split())

blocks = list(map(int,input().split()))
water = 0

for i in range(1,w-1):
    nowh = blocks[i]
    lefth = max(blocks[:i])
    righth = max(blocks[i+1:])
    nowwater = min(righth,lefth)-nowh
    if nowwater > 0:
        water += nowwater

print(water)
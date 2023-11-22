import sys
input = sys.stdin.readline

N, K = map(int, input().split())

target_list = list(map(int,input().split()))

st = 0
end = K
tmp = sum(target_list[:K])
maxv = tmp

for i in range(K,N):
    tmp += target_list[i]
    tmp -= target_list[i-K]
    maxv = max(maxv,tmp)

print(maxv)
import sys
input = sys.stdin.readline

N, X = map(int,input().rstrip().split())

visitors = list(map(int, input().rstrip().split()))

st = -1
end = X-1

tmp_sum = sum(visitors[:X])
max_sum = sum(visitors[:X])
max_num = 1

for i in range(N-X):
    st += 1
    end += 1
    tmp_sum = tmp_sum + visitors[end] - visitors[st]
    if tmp_sum == max_sum:
        max_num += 1
    elif tmp_sum > max_sum:
        max_sum = tmp_sum
        max_num = 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_num)
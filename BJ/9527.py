import math
import sys

sys.setrecursionlimit(10**8)

a,b = map(int,input().split())

# 주어진 숫자가 2의 제곱수라면, 그 숫자의 1 갯수는 1이다. (100, 1000, 10000)
# 2의 제곱수라면, 그 숫자까지의 1의 갯수 합은 n*2^(n-1) [n은 제곱수] 이다.
# 2의 제곱수가 아니라면, 가까운 제곱수까지의 합 + 차이 + 차이까지의 합 이다.

def sum_one(target_num):
    if target_num <= 0:
        return 0
    
    n = int(math.log2(target_num))
    tmp_num = 2**n
    
    if target_num == tmp_num:
        return int(n*(2**n)/2)+1
    
    diff = target_num-tmp_num
    
    return sum_one(tmp_num)+diff+sum_one(diff)
    
        

print(sum_one(b)-sum_one(a-1))

# 참고 블로그 : https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-9527-1%EC%9D%98-%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0
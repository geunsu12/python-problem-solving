import sys

input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

for j in range(len(word2)):
    for i in range(len(word1)):
        if word1[i] == word2[j]:
            dp[j+1][i+1] = dp[j][i]+1
        else:
            dp[j+1][i+1] = max(dp[j][i+1],dp[j+1][i])

print(dp[-1][-1])

# 알고리즘 LCS
# 참고 사이트 : 
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#longest-common-subsequence-substring
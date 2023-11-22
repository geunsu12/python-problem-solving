import sys

input = sys.stdin.readline

n = int(input())
words = []

for i in range(n):
    words.append([i,input().rstrip()])

sortedWords = sorted(words, key = lambda x:x[1])

max_length = 0
s = n
t = n
candi = []

def getCommonPrefixLength(word1,word2):
    result = 0
    for i in range(min(len(word1),len(word2))):
        if word1[i] == word2[i]:
            result += 1
        else:
            break
    if result == max(len(word1),len(word2)):
        result = -1
    return result

for i in range(n-1):
    tmp = getCommonPrefixLength(sortedWords[i][1],sortedWords[i+1][1])
    # print(sortedWords[i][1], sortedWords[i+1][1], tmp)
    if tmp > max_length:
        candi = [set([sortedWords[i][0],sortedWords[i+1][0]])]
        max_length = tmp
    elif tmp == max_length:
        isInCandi = False
        for each_can in candi:
            if sortedWords[i][0] in each_can or sortedWords[i+1][0] in each_can:
                each_can.add(sortedWords[i][0])
                each_can.add(sortedWords[i+1][0])
                isInCandi = True
        if isInCandi == False:
            candi.append(set([sortedWords[i][0],sortedWords[i+1][0]]))
    # print(candi)

for each_can in candi:
    list_can = sorted(list(each_can))
    if s > list_can[0]:
        s = list_can[0]
        t = list_can[1]
        
print(words[s][1])
print(words[t][1])

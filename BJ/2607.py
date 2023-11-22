n = int(input())
words = []
ans = 0

for i in range(n):
    words.append(input())

def getSimilarity(word1, word2):
    if len(word1)-len(word2) > 1:
        return False
    dic1 = {}
    dic2 = {}
    differ = 0

    for a in word2:
        if a in dic2.keys():
            dic2[a] += 1
        else:
            dic2[a] = 1

    for a in word1:
        # print(a, dic2)
        if a in dic2.keys():
            if dic2[a] > 0:
                dic2[a] -= 1
            else:
                differ += 1
        else:
            differ += 1

    if differ <= 1:
        return True
    else:
        return False

for i in range(1,len(words)):
    if len(words[0]) > len(words[i]):
        if(getSimilarity(words[0],words[i])):
            # print("sim")
            ans += 1
    else:
        if(getSimilarity(words[i],words[0])):
            # print("sim")
            ans += 1
    # print("next")

print(ans)
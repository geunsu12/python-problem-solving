string = input()

numA = 0
for a in string:
    if a == 'a':
        numA += 1

st = 0
end = numA
numWinB = 0
for i in range(end):
    if string[i] == 'b':
        numWinB += 1
minV = numWinB
string = string+string
for i in range(len(string)-end-1):
    if string[st] == 'b':
        numWinB -= 1
    if string[end] == 'b':
        numWinB += 1
    minV = min(minV,numWinB)
    st+=1
    end+=1

print(minV)
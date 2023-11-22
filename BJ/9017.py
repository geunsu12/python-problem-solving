import sys
input = sys.stdin.readline

testCase = int(input())

def eachCase():
    n = int(input())
    scores = list(map(int,input().rstrip().split(' ')))
    # [0,0] -> 점수, 인원
    teams = max(scores)
    scoreList = [[0,0] for _ in range(teams+1)]
    for i,score in enumerate(scores):
        scoreList[i][1] += 1
        if scoreList[i][1] < 5:
            scoreList[i][0]+= score
    scoreList.sort(reverse = True)
    print(scoreList)

    max_team = 0

    
    sorting = sorted(scoreList)
    max_team = [] 
    
    for i in range(len(sorting)):
        if sorting[i][0] == sorting[0][0]:
            max_team.append(i)
        else:
            break
    
    for i in range(len(scores)):
        if i in max_team:
            print(i)
            exit(0)


    return scoreList[0]

for t in range(testCase):
    print(eachCase())
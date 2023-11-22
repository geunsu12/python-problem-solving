t = int(input())

# 2
# superaquatornado
# 2
# 4, 8
# abcdefghijklmnopqrstuvwxyz
# 5

def findShortSen(sen, n):
    ans = n
    
    while ans <= len(sen):
        dict = {a: 0 for a in 'abcdefghijklmnopqrstuvwxyz'}
        st = 0
        end = ans
        
        for i in range(end):
            dict[sen[i]] += 1

        if n in dict.values():
            return ans
        
        while end < len(sen):
            dict[sen[st]] -= 1
            dict[sen[end]] += 1
            st += 1
            end += 1
            if n in dict.values():
                return ans
        ans += 1
    return -1

def findLongSen(sen, n):
    ans = len(sen)
    
    while ans >= n:
        dict = {a: 0 for a in 'abcdefghijklmnopqrstuvwxyz'}
        st = 0
        end = ans
        
        for i in range(end):
            dict[sen[i]] += 1

        if n in dict.values() and sen[st] == sen[end-1]:
            return ans

        while end < len(sen):
            dict[sen[st]] -= 1
            dict[sen[end]] += 1
            st += 1
            end += 1
            for a in dict.keys():
                if dict[a] == n and sen[st] == a and sen[end-1] == a:
                    return ans
        ans -= 1
    return -1

for tc in range(t):
    sen = list(input())
    n = int(input())
    short = findShortSen(sen,n)
    long = findLongSen(sen,n)
    if short == long:
        print(-1)
    else:
        print(short, long)
    
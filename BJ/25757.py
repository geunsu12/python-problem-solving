import sys

input = sys.stdin.readline
dic = {'Y': 2, 'F': 3, 'O': 4}
n, game = input().split(' ')
players = set()
n = int(n)
for i in range(n):
    players.append(input())

print(int(len(players)/dic[game]))

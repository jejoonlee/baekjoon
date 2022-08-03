from pprint import pprint

import sys
sys.stdin = open('input.txt', 'r')


G = int(input())
scores = [[], [], []]
t_score = []

for g in range(G):
    a, b, c = map(int, input().split())
    scores[0].append(a)
    scores[1].append(b)
    scores[2].append(c)

for i in range(G):
    score = 0
    for j in range(3):
        if scores[j].count(scores[j][i]) == 1:
            score += scores[j][i]
    t_score.append(score)

for i in t_score:
    print(i)
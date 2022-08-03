from pprint import pprint

import sys
sys.stdin = open('input.txt', 'r')


# G = int(input())
# scores = [[], [], []]
# t_score = []

# for g in range(G):
#     a, b, c = map(int, input().split())
#     scores[0].append(a)
#     scores[1].append(b)
#     scores[2].append(c)

# for i in range(G):
#     score = 0
#     for j in range(3):
#         if scores[j].count(scores[j][i]) == 1:
#             score += scores[j][i]
#     t_score.append(score)

# for i in t_score:
#     print(i)


T = int(input())

matrix = [[], [], []]

for t in range(T):
    a, b, c = map(int, input().split())
    matrix[0].append(a)
    matrix[1].append(b)
    matrix[2].append(c)

pprint(matrix)
# [[100, 100, 63, 99, 89], 
#  [99, 97, 89, 99, 97], 
#  [98, 92, 63, 99, 98]]

scores = []

for i in range(T):
    score = 0
    for j in range(3):
        if matrix[j].count(matrix[j][i]) == 1:
            score += matrix[j][i]
    scores.append(score)
    # [0, 92, 215, 198, 89]

print(scores)
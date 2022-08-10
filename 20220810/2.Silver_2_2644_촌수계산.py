import sys
sys.stdin = open('input.txt', 'r')

# N = 촌수
N = int(input())

visited = [False] * (N + 1)

per_1, per_2 = map(int, input().split())

# M = 관계의 개수
M = int(input())

links = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    links[v1].append(v2)
    links[v2].append(v1)

print(links)
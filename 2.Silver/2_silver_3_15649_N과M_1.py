import sys

sys.stdin = open("input.txt")

from itertools import permutations

N, M = map(int, input().split())

num_list = [num for num in range(1, N + 1)]

for nums in permutations(num_list, M):
    print(" ".join(map(str, list(nums))))

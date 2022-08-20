import sys
sys.stdin = open('input.txt')

# 시간 초과...

# N = int(input())

# lst = list(map(int, input().split()))
# result = [0] * N

# # 중복 값들을 없앤다
# nums = set(lst)
# nums = list(nums)

# # 이중 리스트를 통해 중복 값을 없앤 값들과, 입력 값들을 비교한다
# for i in range(N):
#     for j in range(len(nums)):
#         if lst[i] > nums[j]:
#             result[i] += 1

# print(*result)
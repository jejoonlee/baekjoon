# 키와 몸무게가 모두 커야 덩치가 더 큰 것
# 자신보다 더 덩치가 큰 사람들이 있으면 k + 1

N = int(input())
# 사람 수

lst = []
for i in range(N):
    x, y = map(int, input().split())
    #키와 몸무게
    lst.append((x, y))
    #[(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

rank = 0
rank_list = []

# 모든 사람들을 비교하기 위한 이중 반복문
for a in range(N):
# N명 중 각자의 키와 몸무게를 가지고 온다
    A = lst[a]
    for b in range(N):
    # N명 안에 각자의 키와 몸무게를 또 가지고 온다
    # 비교를 하기 위해
        B = lst[b]
        if A[0] > B[0] and A[1] > B[1]:
        # 각자의 키는 키끼리, 몸무게는 몸무게끼리 비교한다
        # 만약 키와 몸무게가 더 큰 사람이 있을 경우 rank + 1을 한다
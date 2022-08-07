# 델타 이동 / 델타 탐색
# 한 데이터 기준으로 '상하좌우'를 탐색
# 상 y = y - 1 / 하 y = y + 1 / 좌 x = x - 1/ 우 x = x + 1

# 탐색을 한 후 지뢰가 있으면, 지뢰 수에 1을 누적한다

import sys
sys.stdin = open('input.txt', 'r')

def pprint(list_):
    for row in list_:
        print(row)


N = int(input())

mine_field = [list(input()) for _ in range(N)]
sel = [list(input()) for _ in range(N)]
ans = [['.'] * N for _ in range(N)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1] # column
dy = [-1, -1, -1, 0, 0, 1, 1, 1] # row


# 순회는 아무 방향
for y in range(N):
    for x in range(N):
        bomb = 0     
        for a in range(8):
            sx = dx[a] + y
            sy = dy[a] + x

            if sel[y][x] == 'x':
            # 리스트에서 벗어나면 안됨
                if 0 <= sx < N and 0 <= sy < N:
                    if mine_field[sx][sy] == '*':
                        bomb += 1
                    # ans 변수에 지뢰 개수 저장하기
                    ans[y][x] = bomb

        if mine_field[y][x] == '*':
        # sel 리스트에서 x인데, mine_field에서 지뢰면
            for a in range(N):
                for b in range(N):
                    if mine_field[y][x] == '*':
                        ans[y][x] = '*'

for i in range(N):
    for j in range(N):
        print(ans[i][j], end = '')
    print()
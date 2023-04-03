import sys
sys.stdin = open('input.txt')

N = int(input())

board = [[0] * N for _ in range(N)]

count = 0



def is_possible(row, column, attack):

    dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

    board[row][column] = attack

    for i in range(8):
        sr, sc = row + dr[i], column + dc[i]

        if 0 <= sr < N and 0 <= sc < N:

            if attack == 'X':
                if board[sr][sc] != 0:
                    break

                else:
                    while 0 <= sr < N and 0 <= sc < N:
                        board[sr][sc] = attack
                        sr, sc = sr + dr[i], sc + dc[i]

            if attack == 0:
                if board[sr][sc] == 0:
                    break

                else:
                    while 0 <= sr < N and 0 <= sc < N:
                        board[sr][sc] = attack
                        sr, sc = sr + dr[i], sc + dc[i]


cnt = 0

def search(row, column, queens):

    

    if queens == N:

        global cnt

        cnt += 1
        return

    if row == N:
        return
    
    if column == N:
        search(row + 1, 0, queens)
        return
    
    if board[row][column] != 0:
        search(row, column + 1, queens)
        return

    is_possible(row, column, 'X')
    search(row, column + 1, queens + 1)
    is_possible(row, column, 0)
            

for i in range(N):
    for j in range(N):
        search(i, j, 1)

print(cnt)
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

def square(i, j, length):
    
    for r in range(i, length + i):
        for c in range(j, length + j):
            if matrix[r][c] == 0:
                return False
            
    return True

matrix = [list(map(int, input())) for _ in range(N)]


l = N


while l > 0:

    flag = False

    for i in range(N):
        if flag == True:
            break


        for j in range(M):

            if i + l <= N and j + l <= M:
                flag = square(i, j, l)

                if flag == True:
                    break

            else:
                break
    
    if flag == True:
        break
    else:
        l -= 1


print(l * l)
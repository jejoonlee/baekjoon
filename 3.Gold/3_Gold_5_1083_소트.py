import sys
sys.stdin = open('input.txt')

N = int(input())
array = list(map(int, input().split()))
swap = int(input())

while swap != 0:
    for i in range(1, N):
        if array[i-1] < array[i]:
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            break

    swap -= 1

print(' '.join(map(str, array)))
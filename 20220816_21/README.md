# 20220816 ~ 20220821



## Brute Force

### 1018 체스판 다시 칠하기

```python
M, N = map(int, input().split())

board = [list(input()) for _ in range(M)]

cnt_lst = []

# 탐색을 두번 한다
# 먼저 큰 행열에 이중 for문을 넣는다
for row in range(M - 7):
    for column in range(N - 7):

        # 무조건 [row][column]이 검정이라고, 검정으로 시작 안 해도 된다
        cnt_1, cnt_2 = 0, 0

        # 8 * 8 chess판을 비교하는 것으로, 작게 for문을 돈다
        # 그리고 조건문에 따라 결과가 나오게 한다
        for r in range(row, row + 8):
            for c in range(column, column + 8):

                if 0 <= r < M and 0 <= c < N:
                    # 짝수가 흰색이어야 할 경우,
                    # 짝수에 검정, 그리고 홀수에 흰색이 있으면 1을 누적시킨다
                    if (r + c) % 2 == 0 and board[r][c] != 'W':
                        cnt_1 += 1
                    if (r + c) % 2 == 1 and board[r][c] != 'B':
                        cnt_1 += 1
                    
                    # 짝수가 검정이어야 할 경우
                    # 짝수에 흰색, 그리고 홀수에 검정이 있으면 1을 누적시킨다
                    if (r + c) % 2 == 0 and board[r][c] != 'B':
                        cnt_2 += 1
                    if (r + c) % 2 == 1 and board[r][c] != 'W':
                        cnt_2 += 1

        cnt_lst.append(min(cnt_1, cnt_2))

print(min(cnt_lst))
```

#### 🚨🚨🚨**큰 행열을 순회하면서, 작은 행열 (8*8)을 순회한다**🚨🚨🚨

- **꼭 시작이 검정이라고, 검흰 패턴으로 갈 필요가 없다**
- 색깔을 바꿀때마다 카운트를 해주고, 제일 적게 카운트를 결과로 출력한다





### 정렬

### 11651 좌표 정렬하기

```python
N = int(input())

arr = []
for n in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
    
arr.sort(key = lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])
```

#### 🚨🚨🚨key = lambda 사용🚨🚨🚨

- `key = lambda`를 통해서 어느 부분을 먼저 정렬할 것인지 설정을 한다



### 1181 단어 정렬

```python
N = int(input())

words = set()
for n in range(N):
    word = input()
    words.add(word)

words = list(words)

words.sort()
words.sort(key = len)

for i in words:
    print(i)
```

- `set`를 사용해서 중복을 없앤다
- `words.sort()`를 통해서 알파벳 별로 정렬을 한다
- `words.sort(key = len)` 을 통해서 알파벳 개수에 따라 정렬을 한다




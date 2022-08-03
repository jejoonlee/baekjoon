# ✍️ 문제풀이

[후기](#후기)

[1236 성 지키기](#1236-성-지키기)

[5533 유니크](#5533-유니크)





## 후기

>행열을 배운 첫 날이지만, 많이 어려웠다.
>
>행열을 만드는건 알겠는데, 활용하는게 많이 어려웠다. 더 연습해야 할 것 같다.
>
>특히 이중 for문을 쓸 때에, 기준점이랑 비교점을 잘 써야할거 같은데... 어렵다 ㅜ.ㅜ



## 백준 풀이



### 1236 성 지키기

```python
N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

# 각 행과 열에 X가 존재하면 X를 1로 바꿔준다
# 그리고 각각 행과 열에 있는 1들을 더했는데, 0이 나오면
# 각각 행과 열에 1씩 더해준다.
# 그 행과 열의 값 중 제일 큰 값이 답이다

column = [0] * M
row = [0] * N

for i in range(len(castle)):
    for j in range(len(castle)):
        if castle[i][j] == 'X':
            row[i] = 1
            column[j] = 1

col_cnt = 0
row_cnt = 0

for i in row:
    if i == 0:
        row_cnt += 1

for j in column:
    if i == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))

---------------------------------------------
N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

row = 0
for i in range(N):
# i는 열 'N'의 인덱스
    if 'X' not in castle[i]:
    # 열에 X가 없으면 1씩 더해주기
        row += 1

column = 0
for j in range(M):
# j가 기준점이 되는 것
# 2중 for문
    if 'X' not in [castle[i][j] for i in range(N)]:
        column += 1

print(max(row, column))
```

- 두 번째 식에서

  - row를 구할 때에는 그냥 평소대로 'X'의 유무를 찾는다

  - column에서는 이중 for문을 써야 한다

    - `j`가 기준점이 되는 것이고, `[castle[i][j] for i in range(N)]` 는 

      ```python
      for j in range(M):
          for i in range(N):
              print(castle[i][j])
      ```

      와 같다!




### 5533 유니크

```python
G = int(input())
scores = [[], [], []]
# 게임을 3번씩 한다.
# 게임 별로 숫자가 정해진다
t_score = []
# 각자의 점수가 't_score'에 들어간다

for g in range(G):
    a, b, c = map(int, input().split())
    scores[0].append(a)
    scores[1].append(b)
    scores[2].append(c)

for i in range(G):
    score = 0
    for j in range(3):
        if scores[j].count(scores[j][i]) == 1:
        # .count를 써서 scores[j]에 점수가 하나만 존재하면
            score += scores[j][i]
            # 그 점수를 더해준다
            # 여기서 score은 'i' 기준이다
    t_score.append(score)
    # 더한 숫자를 t_score에 넣어준다

for i in t_score:
    print(i)
```

#### 🚨 중요 포인트🚨

- `for i in range(G)` 는 기준점이다.
  - 즉 `for j in range(3)` 에서 반복하는 점수들을 0으로 만들고, `i` 기준으로 점수들을 더해준다
- `for j in range(3)`에서 `.count`를 써서 해당 점수 `scores[j][i]`가 `scores[j]` 기준  1만 존재하면, score에 점수를 더해준다

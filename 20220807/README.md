# 🧑‍💻 문제 풀이

전체는 아님

[박스 matrix](#박스)

[지뢰 찾기 (Matrix)](#지뢰-찾기)



### 박스

```python
T = int(input())

for t in range(T):
# 열고 행 입력 받기
    N, M = map(int, input().split())

    # 행열 만들기
    area = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 1. 행을 기준으로 순회하기 (밑에서 위로)
    for x in range(M):
        for y in range(N - 1, -1, -1):
    # 상자가 발견될 경우 밑에 공간이 없어질 때까지 밑으로 보냄
            if area[y][x] == 1:
                while True:
            # 리스트 밖으로 나가면 안 됨           
                        if y + 1 == N:
                            break
                        elif area[y + 1][x] == 0:
                            area[y][x] = 0
                            area[y + 1][x] = 1
                            cnt += 1
                        y += 1
                        # 이게 없으면 if와 elif문이 무한 반복
                        # y를 1씩 더해줘서 break를 하게 만들어야 한다
                        # 즉 1 밑에 0이 있으면, 1을 0밑으로 계속 보내되
                        # 1 밑에도 1이 있으면 y가 1씩 커져서, 
                        # if문의 조건과 만족하게 된다
    print(cnt)
```

#### 🚨🚨 중요 ! 🚨🚨

- 아래에서 위로 순회를 해야 한다
- `if y + 1 == N:`  list out of range를 해결
  - 아래에서 위로 순회하는 것이라서 `y + 1 `을 통해 밑이 제한된 공간일 때, `break`를 걸어 건너 뛴다



### 지뢰 찾기

```python
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
```

- Delta 탐색 활용법 (더 익숙해지기...)

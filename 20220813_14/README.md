# ✍️ 문제풀이

[2615 오목](#1543-오목)

[2644 촌수계산](#2644-촌수계산)







## 백준 풀이

### 2615 오목

![오목](README.assets/오목.png)

```python
area = [list(map(int, input().split())) for _ in range(19)]

dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

Flag = False

for r in range(19):
    for c in range(19):

        if area[r][c] == 1 or area[r][c] == 2:

            for i in range(4):
                cnt = 1

                sr = r + dr[i]
                sc = c + dc[i]
                
                # 탐색 중 값이 똑같은 방향이 나오면 그 방향으로 탐색을 시작
                while (0 <= sr < 19 and 0 <= sc < 19) and area[r][c] == area[sr][sc]:

                    # 그리고 연속된 수로 cnt에 1을 누적시키기
                    cnt += 1
                    # 똑같은 방향을 탐색 
                    sr = sr + dr[i]
                    sc = sc + dc[i]

                if cnt == 5:
                    # 기준점에서 뒤에 점의 값을 확인 하는 것
                    br = r - dr[i]
                    bc = c - dc[i]

                    if not(0 <= br < 19 and 0 <= bc < 19) or area[r][c] != area[br][bc]:
                        print(area[r][c])
                        print(r + 1, c + 1)
                        
                        Flag = True


if Flag == False:
    print(0)
```

#### 🚨🚨 Main Point 🚨🚨

**델타 탐색을 이용하지만, 모든 방면을 탐색할 필요는 없다**

- 오른쪽 위, 오른쪽, 오른쪽 아래, 그리고 아래만 탐색한다.
- 4 방면 중, 같은 값이 있다면, 그 방면으로 또 탐색한다
  - 같은 값이 연속으로 있으면, 해당 방면으로 멈출 때까지 탐색을 한다
  - `sr = sr + dr[i]` / `sc = sc + dc[i]`
- 만약 5번 연속이 된다면 또 조건문을 들고 온다
  - 기준 점 `area[r][c]`  뒤에 같은 값이 없어야 해당 돌이 승리를 한다



### 2644 촌수계산

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

```python
# 전체 사람의 수
n = int(input())

# 서로 다른 두 사람들의 번호
per_1, per_2 = map(int, input().split())

#관계 개수
m = int(input())

# 관계 인접 리스트
relation = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    relation[v1].append(v2)
    relation[v2].append(v1)

# 아는 관계
know = [False] * (n + 1)

# dfs 만들기

stack = [(per_1, 0)]
know[per_1] = True

while len(stack) != 0:
    current, count = stack.pop()

    if current == per_2:
        break
    
    for cur in relation[current]:
        if know[cur] == False:
            know[cur] = True
            stack.append((cur, count + 1))
    

if know[per_2] == True:
    print(count)
else:
    print(-1)
```

#### 🚨🚨 Main Point 🚨🚨

**DFS를 쓰되, 튜플을 이용하셔, 촌수를 센다**

- DFS는 스택을 이용한다.
  - 시작점으로 시작해서, 시작점의 인접 정점들을 찾는다
    - 인접 정점들을 방문했다는 것을 저장한다 `False` 에서 `True`로
  - 그리고 그 인접 정점들을 스택에 넣는다
- 여기서 다른 것은, 끝나는 점이 주어진다
  - 그 점을 발견하면, `while문`을 끝내고, 정답인 촌수를 찾는다
- 촌수는 튜플로, 정점과 같이 저장을 한다.
  - 즉 한 정점을 기준으로 인접 정점들이 저장이 될 때에, 촌수는 1 누적 된다

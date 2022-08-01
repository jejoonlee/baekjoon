# 🧑‍💻 문제 풀이

전체는 아님

[10773 제로 (stack, 스택)](#%EF%B8%8F-10773-제로)

[2161 카드 1](#%EF%B8%8F-2161-카드-1)

[23253 자료구조는 정말 최고야](#%EF%B8%8F-23253-자료구조는-정말-최고야)

[9012 괄호 (스택)](#%EF%B8%8F-9012-괄호)

[14720 우유 축제 (이어지는 같은 값 더하기)](#%EF%B8%8F-14720-우유-축제)



### ✔️ 10773 제로

```python
K = int(input())

lst = []
for k in range(K):
    num = int(input())
    lst.append(num)

# 스택이라는 리스트를 만든다
stack = []
for num in lst:
    # num 즉 lst에서 가지고 온 값이 0이 아니면
    # 'stack'에 값을 넣는다
    if num != 0:
        stack.append(num)
    # 반대로 '0'이면, 스택에 있는 마지막 수를 뺀다
    else:
        stack.pop()



print(sum(stack))
```

#### 🚨🚨🚨중요 포인트🚨🚨🚨

- `.pop()` 을 하면 리스트 안에 마지막 값을 빼는 것
  - 해당 값이 0이 아니면 리스트 안에 값을 넣는다
  - 0이면 리스트 안에 있는 마지막 수, 즉 제일 마지막으로 들어간 수(최신 값)를 빼낸다



### ✔️ 2161 카드 1

N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다

```python
from collections import deque

# input() 값
N = int(input())

ori = []
# 리스트 안에 1부터 N까지의 숫자 넣기
for n in range(1, N + 1):
    ori.append(n)

# 변수 이름이 ori 이었던 리스트를 queue로 바꾸고
# deque를 쓸 수 있게 만든다
queue = deque(ori)


# 바닦으로 버린 카드를 new 리스트에 넣는다
new = []

while len(queue) > 1:
# 리스트 queue의 값의 개수가 1이 될때까지
# while문을 돌게 한다
    new.append(queue[0])
    # 제일 앞의 숫자를 바닦으로 버린다
    # 여기서는 new 라는 리스트에 넣는다
    queue.popleft()
    # 그리고 그 숫자를 .popleft()를 통해 뺀다
    queue.append(queue[0])
    # 새로운 첫 번째 숫자열 맨 뒤에 넣는다
    queue.popleft()
    # 그리고 그 숫자도 없앤다

print(*new, *queue)
```

- `deque`를 이용해 문재를 풀었음
- `.popleft() `메서드를 통해 앞의 숫자를 뺐고
- `.append()` 메서드를 통해 맨 뒤에 숫자를 넣었다



### ✔️ 23253 자료구조는 정말 최고야

```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos = []
for m in range(M):
    qty = int(input())
    # 입력한 책 번호들을 리스트 안에 넣는다
    b_num = list(map(int, input().split()))
    for i in range(len(b_num) - 1):
        # 앞에 번호가 더 클 경우 '1'을 pos 리스트에 넣는다
        if b_num[i] > b_num[i + 1]:
            pos.append(1)
        # 그 외에는 '0'을 pos 리스트에 넣는다
        else:
            pos.append(0)

# '0'이 하나라도 있으면 No 를 출력
if 0 in pos:
    print('No')
else:
    print('Yes')
```

- 책 번호들을 리스트에 넣고, 뒤에 번호들과 비교한다

- 꺼낸 번호 순서대로 나열해야 하기 때문에, 제일 뒤에 있는 숫자가 제일 작아야 하고, 번호 순서는 내림차순으로 있어야 한다.

- `for i in range(len(b_num) - 1)`

  - 2개를 비교할 때에는 `- 1` 
  - 3개는 비교할 때에는 `-2` 

  

### ✔️ 9012 괄호

```python
num = int(input())

for n in range(num):
    stack = []
    brk = input()
    for b in brk:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
```

- `stack` 이라는 리스트를 만든다
- `b`가 `(` 면 스택에 넣는다
- 반대로 `b`가 `)` 면 두 가지 상황이 주어지는데
  - `stack` 리스트 안에 값이 존재하면, 그 안에 있는 값을 하나 빼준다
  - 없으면 바로 NO를 출력하고 그만한다
-  모두 끝나면 `stack`에 아무것도 없으면 YES를 출력하고
  - 값이 존재하면 NO를 출력해준다



### ✔️ 14720 우유 축제

```python
num = int(input())

sum = 0
store = list(map(int, input().split()))

for i in range(num):
    if store[i] == sum % 3:
    # '0, 1, 2', 3개의 값들이 순차적으로 있어야, sum이 1씩 누적 된다
    # sum이 1씩 누적 될때마다 나머지는 '0, 1, 2' 순으로 바뀐다
        sum += 1

print(sum)

```


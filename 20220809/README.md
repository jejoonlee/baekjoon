# ✍️ 문제풀이

[후기](#후기)

[1371 가장 많은 글자](#1371-가장-많은-글자)

[1526 가장 큰 금민수](#1526-가장-큰-금민수)





## 백준 풀이



### 1371 가장 많은 글자

```python
al = {}

code = [0] * 26

while True:
    try:
        sen = input()
        for s in sen:
            if s == ' ':
                continue
            else:
                code[ord(s) - 97] += 1

        # code에서 제일 큰 값을 가지고 온다
        max_value = max(code)

        final = []
        for c in range(len(code)):
            # 코드의 c 번째에 있는 값이 max_value와 같다면
            if code[c] == max_value:
                # final 리스트에 유니코드에서 알파벳으로 변형된 값을 넣은다
                final.append(chr(c + 97))

    except EOFError:
        break

result = ''.join(final)
print(result)N, M = map(int, input().split())

cards = list(map(int, input().split()))

max_num = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            # 3중문으로 한번씩 더해준다
            num = cards[i] + cards[j] + cards[k]

            # M보다 작을 경우는 계속 위의 공식을 진행한다
            if max_num < num <= M:
                # num이 max_num보다 크면 max_num은 num의 값이 된다
                max_num = num

print(max_num)
```





### 1526 가장 큰 금민수

```python
N = int(input())

gms = []
# 작거나 같은 => + 1

num = 40

while num != N:
    flag = True
    num += 1

    nums = str(num)

    for i in range(len(nums)):
        if nums[i] == '4' or nums[i] == '7':
            pass
        else:
            # 4, 7이 아예 없다면 flag는 False로 저장된다
            # 그렇게 저장되면, 아래 if 조건문과 성사가 안 되서
            # 다시 while문 시작점으로 돌아간다
            flag = False

    if flag:
        gms.append(num)

print(max(gms))

----------------------------------------------------------------
# 제일 큰 수에서 'N' 아래로 내려가면서 최대값을 구하는 코드


N = int(input())

# 작거나 같은 => + 1

while True:
    flag = True

    nums = str(N)

    for i in range(len(nums)):
        if nums[i] == '4' or nums[i] == '7':
            pass
        else:
            # 4, 7이 아예 없다면 flag는 False로 저장된다
            # 그렇게 저장되면, 아래 if 조건문과 성사가 안 되서
            # 다시 while문 시작점으로 돌아간다
            flag = False
            N -= 1
            # 최대값을 구하기 때문에, 내려오면서 계산한다
            # 예를 들어 100부터 시작해서, flag가 False이면
            # N에 1일 빼준다

    if flag:
        print(N)
        break
```


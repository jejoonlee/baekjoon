# 🧑‍💻 백준

|   날짜   |     단계      |                             제목                             | 진행 현황  |
| :------: | :-----------: | :----------------------------------------------------------: | :--------: |
| 7월 6일  |  [1-1](#1-1)  |     [Hello World](https://www.acmicpc.net/problem/2557)      | `진행완료` |
| 7월 6일  |  [1-2](#1-2)  |    [We love krii](https://www.acmicpc.net/problem/10718)     | `진행완료` |
| 7월 7일  |  [1-3](#1-3)  |       [고양이](https://www.acmicpc.net/problem/10171)        | `진행완료` |
| 7월 8일  |  [1-4](#1-4)  |         [개](https://www.acmicpc.net/problem/10172)          | `진행완료` |
| 7월 11일 |  [1-5](#1-5)  |         [A+B](https://www.acmicpc.net/problem/1000)          | `진행완료` |
| 7월 11일 |  [1-6](#1-6)  |         [A-B](https://www.acmicpc.net/problem/1001)          | `진행완료` |
| 7월 11일 |  [1-7](#1-7)  |         [AxB](https://www.acmicpc.net/problem/10998)         | `진행완료` |
| 7월 11일 |  [1-8](#1-8)  |         [A/B](https://www.acmicpc.net/problem/1008)          | `진행완료` |
| 7월 12일 |  [1-9](#1-9)  |      [사칙연산](https://www.acmicpc.net/problem/10869)       | `진행완료` |
| 7월 14일 | [1-10](#1-10) |         [??!](https://www.acmicpc.net/problem/10926)         | `진행완료` |
| 7월 14일 | [1-11](#1-11) | [1998년생인 내가 태국에서는 2541년생?!](https://www.acmicpc.net/problem/18108) | `진행완료` |
| 7월 14일 | [1-12](#1-12) |       [나머지](https://www.acmicpc.net/problem/10430)        | `진행완료` |
| 7월 15일 | [1-13](#1-13) | [곱셈](https://www.acmicpc.net/problem/2588) **int를 list로 바꾸는 방법** | `진행완료` |
| 7월 15일 | [1-14](#1-14) |        [새싹](https://www.acmicpc.net/problem/25083)         | `진행완료` |
| 7월 19일 |  [2-1](#2-1)  |    [두 수 비교하기](https://www.acmicpc.net/problem/1330)    | `진행완료` |
| 7월 19일 |  [2-2](#2-2)  |      [시험 성적](https://www.acmicpc.net/problem/9498)       | `진행완료` |
| 7월 20일 |  [2-3](#2-3)  |         [윤년](https://www.acmicpc.net/problem/2753)         | `진행완료` |
| 7월 21일 |  [2-4](#2-4)  |    [사분면 고르기](https://www.acmicpc.net/problem/14681)    | `진행완료` |
| 7월 22일 |  [2-5](#2-5)  |      [알람 시계](https://www.acmicpc.net/problem/2884)       | `진행완료` |
| 7월 22일 |  [2-6](#2-6)  |      [오븐 시계](https://www.acmicpc.net/problem/2525)       | `진행완료` |
|          |               |                                                              |            |



## 풀이

### 1-1

```python
print('Hello World!')
```

'Hello World!' will be **printed** 

`print`= 출력



[위로가기](#-백준)

### 1-2

```python
print('강한친구 대한육군')
print('강한친구 대한육군')
```



[위로가기](#-백준)

### 1-3

```python
print('\\    /\\')        
print(" )  ( ')")		# '..' 이 겹쳐서 ".."를 사용 함
print('(  /  )')
print(' \\(__)|')
```

- **\ 는 두개가 있어야 backslash(\\\)가 출력이 된다**
- `'....'`를 써도 되지만 `"....."`을 써서 겹치는거 방지 ㅜ.ㅜ



[위로가기](#-백준)

### 1-4

```python
print('|\\_/|\n|q p|   /}\n( 0 )"""\\\n|"^"`    |\n||_/=\\\\__|')
------------------------------------------------------------------

print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')
```



[위로가기](#-백준)

### 1-5

```python
a, b = input().split()
# a 값과 b 값을 공백(split)과 함께 입력한다

print(int(a) + int(b))
# 입력이 된 값 a와 b를 더한다

# 단!!! input()은 문자열이다. 따라서, 숫자를 넣고 싶으면 출력값을 int (integer), 정수로 바꿔줘야 한다
```



[위로가기](#-백준)

### 1-6

```python
a, b = input().split()
print(int(a) - int(b))
```



[위로가기](#-백준)

### 1-7

```python
a, b = input().split()
print(int(a) * int(b))
```



[위로가기](#-백준)

### 1-8

```python
a, b = input().split()
print(int(a) / int(b))
```



[위로가기](#-백준)

### 1-9

```python
a, b = input().split()
a = int(a)                  # int, 정수로 미리 설정을 해둔다
b = int(b)  

print(a + b)
print(a - b)
print(a * b)
print(a // b)               # 몫을 구하는 것이라서 //을 사용한다
print(a % b)
```



[위로가기](#-백준)

### 1-10

```python
a = input()
b = '??!'

print(a + b)		# 공백없이 a와 b가 붙는다
```



[위로가기](#-백준)

### 1-11

```python
y = int(input())
year = y - 543          # 불기연도는 원래 연도에서 543을 더한다.
                        # 반대로 불기연도에서 543을 빼면, 현재 연도가 된다
print(year)             
```



[위로가기](#-백준)

### 1-12

```python
a, b, c = map(int, input().split())

print((a + b) % c)						# 첫째 줄에 (A+B)%C
print(((a % c) + (b % c)) % c)			# 둘째 줄에 ((A%C) + (B%C))%C
print((a * b) % c)						# 셋째 줄에 (A×B)%C
print(((a % c) * (b % c)) % c)			# 넷째 줄에 ((A%C) × (B%C))%C
```



[위로가기](#-백준)

### 1-13

```python
a = int(input())
b = int(input())

c = list(map(int, str(b)))
# int를 list로 바꾸기

print(a * int(c[2]))
print(a * int(c[1]))
print(a * int(c[0]))
print(a * b)
```

**`list(map(int, str(...)))` : int를 list로 바꾸기!**



[위로가기](#-백준)

### 1-14

```python
print('''         ,r'"7''')
print('''r`-_   ,'  ,/''')
print(""" \\. ". L_r'""")
print('   `~\\/')
print('      |')
print('      |')
```



[위로가기](#-백준)

### 2-1

```python
a, b = map(int, input().split())

if a > b:
    print('>')
elif a == b:
    print('==')
else:
    print('<')
```

`if`, `elif`, `else` 이용하기.



[위로가기](#-백준)

### 2-2

```python
a = int(input())

if a < 60:
    print('F')
elif a < 70 :
    print('D')
elif a < 80:
    print('C')
elif a < 90:
    print('B')
else:
    print('A')
```



[위로가기](#-백준)

### 2-3

```python
a = int(input())

if (a % 100 == 0) != (a % 400 == 0):
    print('0')
# a가 100의 배수이지만,
# 400의 배수가 아닐때만 0을 출력
elif (a % 4 == 0):
    print('1')
else:
    print('0')
```



[위로가기](#-백준)

### 2-4

```python
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
```



[위로가기](#-백준)

### 2-5

```python
H, M = map(int, input().split())

m = (H * 60 + M) - 45

wh = m // 60
wm = m % 60

if wh < 0:
    print(wh + 24, wm)
# hour가 0 이하면 24로 더해주기
elif wh > 24:
    print(wh -24, wm)
# hour가 24 이상이면 24로 빼주기
else:
    print(wh, wm)
```



[위로가기](#-백준)

### 2-6

```python
a, b = map(int, input().split())
c = int(input())

m = (a * 60 + b) + c

H = m // 60
M = m % 60

if H < 0:
    print(H + 24, M)
if H >= 24:
    print(H - 24, M)
else:
    print(H, M)
```

- 2-5과 맥락 비슷함



[위로가기](#-백준)




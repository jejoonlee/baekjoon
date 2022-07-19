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



## 풀이

### 1-1

```python
print('Hello World!')
```

'Hello World!' will be **printed** 

`print`= 출력



### 1-2

```python
print('강한친구 대한육군')
print('강한친구 대한육군')
```



### 1-3

```python
print('\\    /\\')        
print(" )  ( ')")		# '..' 이 겹쳐서 ".."를 사용 함
print('(  /  )')
print(' \\(__)|')
```

- **\ 는 두개가 있어야 backslash(\\\)가 출력이 된다**
- `'....'`를 써도 되지만 `"....."`을 써서 겹치는거 방지 ㅜ.ㅜ





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





### 1-5

```python
a, b = input().split()
# a 값과 b 값을 공백(split)과 함께 입력한다

print(int(a) + int(b))
# 입력이 된 값 a와 b를 더한다

# 단!!! input()은 문자열이다. 따라서, 숫자를 넣고 싶으면 출력값을 int (integer), 정수로 바꿔줘야 한다
```





### 1-6

```python
a, b = input().split()
print(int(a) - int(b))
```





### 1-7

```python
a, b = input().split()
print(int(a) * int(b))
```





### 1-8

```python
a, b = input().split()
print(int(a) / int(b))
```





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





### 1-10

```python
a = input()
b = '??!'

print(a + b)		# 공백없이 a와 b가 붙는다
```





### 1-11

```python
y = int(input())
year = y - 543          # 불기연도는 원래 연도에서 543을 더한다.
                        # 반대로 불기연도에서 543을 빼면, 현재 연도가 된다
print(year)             
```





### 1-12

```python
a, b, c = map(int, input().split())

print((a + b) % c)						# 첫째 줄에 (A+B)%C
print(((a % c) + (b % c)) % c)			# 둘째 줄에 ((A%C) + (B%C))%C
print((a * b) % c)						# 셋째 줄에 (A×B)%C
print(((a % c) * (b % c)) % c)			# 넷째 줄에 ((A%C) × (B%C))%C
```





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



### 1-14

```python
print('''         ,r'"7''')
print('''r`-_   ,'  ,/''')
print(""" \\. ". L_r'""")
print('   `~\\/')
print('      |')
print('      |')
```





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


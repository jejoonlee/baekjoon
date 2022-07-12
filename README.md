# 🧑‍💻 백준

|   날짜   |    단계     |                         제목                          | 진행 현황  |
| :------: | :---------: | :---------------------------------------------------: | :--------: |
| 7월 6일  | [1-1](#1-1) |  [Hello World](https://www.acmicpc.net/problem/2557)  | `진행완료` |
| 7월 6일  | [1-2](#1-2) | [We love krii](https://www.acmicpc.net/problem/10718) | `진행완료` |
| 7월 7일  | [1-3](#1-3) |    [고양이](https://www.acmicpc.net/problem/10171)    | `진행완료` |
| 7월 11일 | [1-4](#1-4) |      [A+B](https://www.acmicpc.net/problem/1000)      | `진행완료` |
| 7월 11일 | [1-5](#1-5) |      [A-B](https://www.acmicpc.net/problem/1001)      | `진행완료` |
| 7월 11일 | [1-6](#1-6) |     [AxB](https://www.acmicpc.net/problem/10998)      | `진행완료` |
| 7월 11일 | [1-7](#1-7) |      [A/B](https://www.acmicpc.net/problem/1008)      | `진행완료` |
| 7월 12일 | [1-8](#1-8) |   [사칙연산](https://www.acmicpc.net/problem/10869)   | `진행완료` |



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
a, b = input().split()
# a 값과 b 값을 공백(split)과 함께 입력한다

print(int(a) + int(b))
# 입력이 된 값 a와 b를 더한다

# 단!!! input()은 문자열이다. 따라서, 숫자를 넣고 싶으면 출력값을 int (integer), 정수로 바꿔줘야 한다
```



### 1-5

```python
a, b = input().split()
print(int(a) - int(b))
```



### 1-6

```python
a, b = input().split()
print(int(a) * int(b))
```



### 1-7

```python
a, b = input().split()
print(int(a) / int(b))
```



### 1-8

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


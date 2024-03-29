# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

N, X = map(int, input().split())

A = list(map(int, input().split()))
# 리스트를 만드는데, 리스트 안에 있는 값들은 다 int 이다

li = []

for i in A:
# 'i'는 리스트 A에 있는 값들을 추출해 낸 값
    if i < X:
    # 'x' 값보다 작은 'i'값은
        li.append(i)
        # 'li'라는 리스트에 넣는다

for i in li:
    print(i, end = ' ')
# for 문을 통해서 li(타입 리스트)에 있는 값들을
# 추출해 낸다. 'i'가 추출해 낸 각자 값들
# end = ' ' 를 통해서 한 줄로 출력할 수 있게 한다
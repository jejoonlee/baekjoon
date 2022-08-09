
import sys
sys.stdin = open('input.txt', 'r')

# 각 문자들을 유니코드로 바꿔준다
# 그리고 문자들의 유니코드를 97로 빼서, (code의 인덱스를 구하기 위해서)
# 알파벳 별로 만들어진 code에 1을 누적시킨다

# sen = list(input())

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
print(result)
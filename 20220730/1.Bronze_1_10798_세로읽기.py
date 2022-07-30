import sys
sys.stdin = open('input.txt', 'r')

letters = []
for i in range(5):
    input_ = input()
    leng = len(input_)
    for i in range(leng):
        letters.append(input_[i])
        print(letters)
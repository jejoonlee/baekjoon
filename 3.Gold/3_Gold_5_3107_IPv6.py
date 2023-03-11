import sys
sys.stdin = open('input.txt')

IPv6 = list(input().split(':'))
answer = []
index = 0
add_address = 0

print(IPv6)

if len(IPv6) == 8:
    for i in IPv6:
        answer.append(i.zfill(4))

elif len(IPv6) > 0:
    while len(IPv6) + add_address != 8:

        if len(IPv6[index]) != 0:
            answer.append(IPv6[index].zfill(4))
        else:
            

    pass


print(':'.join(answer))
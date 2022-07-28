# a = input()

# for i in a:
#     if i in ['A', 'B', 'C']:
#         a = a.replace(i, '3')
#     elif i in ['D', 'E', 'F']:
#         a = a.replace(i, '4')    
#     elif i in ['G', 'H', 'I']:
#         a = a.replace(i, '5')
#     elif i in ['J', 'K', 'L']:
#         a = a.replace(i, '6')
#     elif i in ['M', 'N', 'O']:
#         a = a.replace(i, '7')
#     elif i in ['P', 'Q', 'R', 'S']:
#         a = a.replace(i, '8')
#     elif i in ['T', 'U', 'V']:
#         a = a.replace(i, '9')
#     elif i in ['W', 'X', 'Y', 'Z']:
#         a = a.replace(i, '10')

# result = sum(map(int, list(a)))

# print(result)

a = input()

phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0

for i in a:
    for j in phone:
        if i in j:
            result = result + phone.index(j) + 3

print(result)

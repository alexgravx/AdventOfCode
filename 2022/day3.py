file_path = './2022/text3'
Alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

sum = 0

with open(file_path, 'r') as file:
    F = file.read().splitlines()
    F = [i for i in F]


def process(F):
    L = []
    n = 0
    while n < len(F):
        L_int = []
        n2 = 0
        while (n2 < 3) and (n+n2 < len(F)):
            L_int.append(F[n+n2])
            n2 += 1
        if L_int != []:
            L.append(L_int)
        n += n2
    return L


L = process(F)

for i in L:
    for k in i[0]:
        if (k in i[1]) and (k in i[2]):
            sum += Alphabet.index(k) + 1
            break

'''
for i in F:
    part1 = i[:(len(i)//2)]
    part2 = i[(len(i)//2):]

    for k in part1:
        if k in part2:
            sum0 = sum
            sum += Alphabet.index(k) + 1
            break
'''

print(sum)

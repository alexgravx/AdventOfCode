file_path = './2022/text4'

with open(file_path, 'r') as file:
    F = file.read().splitlines()
    F = [i for i in F]

L = []

for i in F:
    i = i.split(',')
    L2 = []
    for k in i:
        k = k.split('-')
        k = [int(j) for j in k]
        L2.append(k)
    L.append(L2)

s = 0


for i in L:
    a = [i for i in range(i[0][0], (i[0][1]+1))]
    b = [i for i in range(i[1][0], (i[1][1]+1))]
    for i in a:
        if i in b:
            s += 1
            break

"""
print(f"Est ce que 2 >= 10 ? {2 >= 10}")

for i in L:
    if (i[0][0] >= i[1][0] and i[0][1] <= i[1][1]):
        s += 1
        print(i)
        print(i[0][0], i[1][0])
        print(i[0][0] >= i[1][0])
    elif (i[0][0] <= i[1][0] and i[0][1] >= i[1][1]):
        s += 1

"""
print(s)

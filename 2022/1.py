with open('/Users/alexandregravereaux/Desktop/AdventofCode/2022/text1', 'r') as file:
    F = file.read().splitlines()
    F = [i for i in F]

L = []
n = 0
while n < len(F):
    L_int = []
    while (n < len(F)) and (F[n] != ''):
        L_int.append(int(F[n]))
        n += 1
    if L_int != []:
        L.append(L_int)
    n += 1

Sommes = [sum(i) for i in L]
Sommes_tri = sorted(Sommes)[::-1]
Total = sum(Sommes_tri[:3])

print(Total)

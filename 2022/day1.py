def opening(file_path):
    with open(file_path, 'r') as file:
        F = file.read().splitlines()
        F = [i for i in F]
    return F


def process(F):
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
    return L


if __name__ == '__main__':
    L = process(opening('./2022/text1'))
    # Question 1
    sommes = [sum(i) for i in L]
    print(max(sommes))
    # Question 2
    sommes_tri = sorted(sommes)[::-1]
    total = sum(sommes_tri[:3])
    print(total)

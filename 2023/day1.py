numbers = '1234567890'
numbers_letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_letters_inv = [i[::-1] for i in numbers_letters]

def extract(file_path):
    L = []
    with open(file_path, 'r') as f:
        L = f.read().splitlines()
    return L

def transform(L):
    Sol = []
    # On récupère uniquement les chiffres de la chaîne de caractères
    L = ["".join(list(filter(lambda x: x in numbers, k))) for k in L]
    # On ne récupère que les premiers et derniers chiffres sous format entier
    for k in L:
        if len(k) == 1:
            Sol.append(int(k*2))
        else:
            Sol.append(int(k[0])*10 + int(k[-1]))
    return sum(Sol)

def split(delimiters, string, maxsplit=0):
    # Fonction pour splitter autour des chiffres (regex)
    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, string, maxsplit)

def replace(chaine, remplacement):
    # Fonction qui replace de gauche à droite les chiffres
    chaine_chiffre = ''
    for j in chaine:
        chaine_chiffre += j
        for k1,k2 in zip(remplacement, numbers):
            chaine_chiffre = chaine_chiffre.replace(k1,k2)
    return chaine_chiffre

def transform2(L):
    # Fonction qui replace le premier et le dernier chiffre apparaissant (de gauche à droite pour le premier et de droite à gauche pour le dernier)
    for i in range(len(L)):
        Decomposition = split(numbers, L[i])
        Decomposition[0] = replace(Decomposition[0], numbers_letters)
        Decomposition[-1] = replace(Decomposition[-1][::-1], numbers_letters_inv)[::-1]
        L[i] = "".join(Decomposition[0]+L[i]+Decomposition[-1])
    result = transform(L)
    return result
    

if __name__ == '__main__':
    print(transform(extract('./2023/text1')))
    print(transform2(extract('./2023/text1')))
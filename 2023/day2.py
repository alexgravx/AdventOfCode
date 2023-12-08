from day1 import extract, split

delimiters = [" ", ":", ",", ";"]
dictionnaire = {'red': 12, 'green': 13, 'blue': 14}

def possible(str_game):
    L_game = [i for i in split(delimiters, str_game) if i != ''][2:][::-1]
    for i in range(len(L_game)):
        if L_game[i] in dictionnaire and int(L_game[i+1]) > dictionnaire[L_game[i]]:
            return False
    return True
    
def result(L):
    Sol = []
    for i in range(len(L)):
        if possible(L[i]):
            Sol.append(i+1)
    return sum(Sol)

if __name__ == '__main__':
    L = extract('./2023/text3')
    print(result(L))
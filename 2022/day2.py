score_objets = {'X': 1, 'Y': 2, 'Z': 3}

score_objectif = {'X': 0, 'Y': 3, 'Z': 6}

result = {'A X': 3, 'A Y': 6, 'A Z': 0, 'B X': 0,
          'B Y': 3, 'B Z': 6, 'C X': 6, 'C Y': 0, 'C Z': 3}


def opening(file_path):
    with open(file_path, 'r') as file:
        F = file.read().splitlines()
        F = [i for i in F]
    return F


def part1(F):
    points = 0
    for i in F:
        points += result[i]
        points += score_objets[i[-1]]
    return points


def part2(F):
    points = 0
    for i in F:
        score = score_objectif[i[-1]]
        points += score
        for (key, value) in result.items():
            if (value == score) and (key[0] == i[0]):
                points += score_objets[key[-1]]
    return points


if __name__ == '__main__':
    F = opening('./2022/text2')
    # Part 1
    print(part1(F))
    # Part 2
    print(part2(F))

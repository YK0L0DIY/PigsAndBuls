import random

from future.moves import itertools


def analyse(result):
    result = list(result)
    bulls = result[0]
    pigs = result[3]
    return int(bulls), int(pigs)


def create_possibilities():
    result = []
    for prod in itertools.permutations(range(10), 4):
        result.append("".join([str(perm) for perm in prod]))
    return result


def random_num():
    num = ""
    while len(num) < 4:
        d = str(int(random.random() * 10))
        if d not in num:
            num = num + d
    return num


def evaluate(possible, selected):
    bulls = 0
    pigs = 0
    for x in range(len(selected)):
        for y in range(len(selected)):
            if selected[x] == possible[x] and x == y:
                bulls = bulls + 1
    for x in range(len(selected)):
        if selected[x] in possible:
            pigs = pigs + 1
    pigs = pigs - bulls
    return bulls, pigs


def remove_from_list(old_list, selected, score):
    new_list = []
    for c in range(len(old_list)):
        if evaluate(old_list[c], selected) == score:
            new_list.append(old_list[c])
    return new_list


total_list = create_possibilities()
tries = []
answers = []
print("SERA QUE ADVINHO?\n")

while True:
    selected = total_list[0]
    if len(tries) == 0:
        selected = random_num()
    tries = tries + [selected]

    score = str(input("Tentativa %2s e %s. como foi? (xT,xP)? " % (len(tries), selected)))
    answers = answers + [score]
    score = analyse(score)

    if score == (4, 0):
        print("ACERTEI!!")
        break
    total_list = remove_from_list(total_list, selected, score)

    if not total_list:
        print("Nenhum numero certo! Batoteiro!")
        break

print("As suas respostas as tentativas foram:")
for x in range(len(tries)):
    print("%s : %s" % (tries[x], answers[x]))

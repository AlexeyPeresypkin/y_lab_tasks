from random import choice


def generate_loses_combinations():
    loses = []
    for i in range(1, 92, 10):
        l = [i for i in range(i, i + 10)]
        [loses.append(l[i:i + 5]) for i in range(6)]
    for i in range(1, 11):
        l = [i for i in range(i, i + 91, 10)]
        [loses.append(l[i:i + 5]) for i in range(6)]
    for i in range(5, 11):
        l = [i for i in range(i, i * 9 + 2, 9)]
        for i in range(len(l) - 4):
            loses.append(l[i:i + 5])
    from_range = 60
    for i in range(96, 91, -1):
        l = [i for i in range(from_range, i + 1, 9)]
        from_range -= 10
        for i in range(len(l) - 4):
            loses.append(l[i:i + 5])
    to_range = 101
    for i in range(1, 7):
        l = [i for i in range(i, to_range, 11)]
        to_range -= 10
        for i in range(len(l) - 4):
            loses.append(l[i:i + 5])
    for i in range(11, 52, 10):
        l = [i for i in range(i, 101, 11)]
        for i in range(len(l) - 4):
            loses.append(l[i:i + 5])
    return loses


# Инициализация карты
maps = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# Инициализация проигрышных вариантов
loses = generate_loses_combinations()


# Вывод карты на экран
def print_maps():
    print_for_matrix = []
    [print_for_matrix.append(maps[i:i + 10]) for i in range(0, 91, 10)]
    s = [[str(e) for e in row] for row in print_for_matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


# Сделать ход в ячейку
def step_maps(step, symbol):
    maps[step - 1] = symbol


# Отменить ход
def revert_step(step):
    maps[step - 1] = step


# Получить текущий результат игры
def get_result():
    for i in loses:

        if all([
            maps[i[0] - 1] == "X",
            maps[i[1] - 1] == "X",
            maps[i[2] - 1] == "X",
            maps[i[3] - 1] == "X",
            maps[i[4] - 1] == "X",
        ]):
            return '0'

        if all([
            maps[i[0] - 1] == "0",
            maps[i[1] - 1] == "0",
            maps[i[2] - 1] == "0",
            maps[i[3] - 1] == "0",
            maps[i[4] - 1] == "0",
        ]):
            return 'X'

    return False


# Предлагаем сделать ход игроку
def step_from_person():
    global step
    variants_to_step = [i for i in maps if str(i) not in 'X0']
    try:
        step = int(input("Введите значение: "))
        if step not in variants_to_step:
            raise ValueError
    except ValueError:
        print(
            f'Неверный ввод, необходимо ввести номер одной из доступных свободных клеток: \n {str(variants_to_step)[1:-1]}')
        step_from_person()


# "Искусственный" интеллект: выбор хода
def AI():
    variants_to_step = [i for i in maps if str(i) not in ('X', 'O')]
    if not variants_to_step:
        return 'draw'
    for variant in range(len(variants_to_step)):
        var = choice(variants_to_step)
        variants_to_step.remove(var)
        step_maps(var, 'O')
        if not get_result():
            revert_step(var)
            return var
        revert_step(var)
    return 'loose'


# Основная программа
game_over = False
human = True

while not game_over:
    # 1. Показываем карту
    print_maps()
    # 2. Спросим у играющего куда делать ход
    if human:
        symbol = "X"
        step_from_person()
    else:
        print("Компьютер делает ход: ")
        symbol = "O"
        step = AI()

    # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то...
    if step == 'draw':
        print("Ничья!")
        game_over = True
        win = "дружба"
    elif step == 'loose':
        print('Ты победил, поздравляю!')
        win = 'X'
        game_over = True
    else:
        step_maps(step, symbol)  # делаем ход в указанную ячейку
        win = get_result()  # определим победителя
        if win:
            game_over = True
        else:
            game_over = False
    human = not human

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)

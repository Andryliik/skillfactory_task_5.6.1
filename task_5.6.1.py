print(" \n"
      "добро пожаловать в игру 'Крестики и нолики'\n"
      "правила игры: игроки по очереди вводят номер строки и столбца через пробел,\n"
      "Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.\n"
      " ")
# Инициализация игровой облости
maps = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
# Инициализация условий победы
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод игрового поля на экран
def print_maps():
    print(" ", "0", "1", "2")
    print("0", maps[0], maps[1], maps[2])
    print("1", maps[3], maps[4], maps[5])
    print("2", maps[6], maps[7], maps[8])


# Сделать ход в ячейку, проверить, занята ли уже клетка
def step_maps(string_maps, column_maps, symbol):
    if 0 <= string_maps <= 2 and 0 <= column_maps <= 2:
        if string_maps == 0:
            if maps[column_maps] == '-':
                maps[column_maps] = symbol
            else: return False
        elif string_maps == 1:
            if maps[column_maps + 3] == '-':
                maps[column_maps + 3] = symbol
            else: return False
        elif string_maps == 2:
            if maps[column_maps + 6] == '-':
                maps[column_maps + 6] = symbol
            else: return False
    else:
        return False


# Получить текущий результат игры
def get_result():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    return win

# основная программа
game_over = False
player1 = True
player2 = False
while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True and player2 == False:
        symbol = "X"
        string_maps, column_maps = input("Игрок 1 (Х), ваш ход: ").split()
    else:
        symbol = "O"
        string_maps, column_maps = input("Игрок 2 (0), ваш ход: ").split()
    string_maps = int(string_maps)
    column_maps = int(column_maps)

    # 3. Проверка вводимых данных на правильность.
    if step_maps(string_maps, column_maps, symbol) == False:
        print("Введены неверные координаты, попробуйте ещё раз")
        player1 = player1
        player2 = player2
    else:
        step_maps(string_maps, column_maps, symbol)
        player1, player2 = not (player1), not (player2)

    # 4. определим победителя
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)

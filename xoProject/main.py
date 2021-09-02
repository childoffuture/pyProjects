# Переменные для хранения параметров игрового поля
width = 0
height = 0
lineSize = 0
field = []
players = [{'name': 'Игрок 1', 'sign': 'X'},
           {'name': 'Игрок 2', 'sign': 'O'}]

# Функция инициализирующая параметры игры (размер поля, длину линии крестиков-ноликов для победы)
def initField():
    flag = False
    global field
    global width
    global height
    global lineSize
    lst = input("Введите параметры игрового поля в формате <ширина>x<высота>x<число знаков для победы> (пример: 3x3x3):").split('x')
    if len(lst) == 3:
        mask = "1234567890"
        if all(i in mask for i in lst[0]):
            if all(i in mask for i in lst[1]):
                if all(i in mask for i in lst[2]):
                    width = int(lst[0])
                    height = int(lst[1])
                    lineSize = int(lst[2])
                    if width >= lineSize or height >= lineSize:
                        print("Размер поля:", width, height)
                        field.clear()
                        for i in range(height):
                            row = []
                            for j in range(width):
                                row.append('_')
                            field.append(row)
                        flag = True
                    else:
                        print("размер поля не соответствует числу знаков для победы")
            else:
                print("Неверное значение высоты")
        else:
            print("Неверное значение ширины")
    else:
        print("Неверный формат данных")
    return flag

# Функция выполняющая ход игрока
def makeMovement(player):
    flag = False
    lst = input(player.get('name') + " : ").split(' ')
    mask = "1234567890"
    if len(lst) == 2 and all(i in mask for i in lst[0]) and all(i in mask for i in lst[1]):
        row = int(lst[0]) - 1
        column = int(lst[1]) - 1
        if 0 <= row < width and 0 <= column < height:
            if field[row][column] == "_":
                field[row][column] = player.get('sign')
                flag = True
            else:
                print("Клетка (", row+1, ";", column+1, ") занята")
        else:
            print("Неверный номер клетки")
    else:
        print("Неверная команда. Введите номер клетки в формате <номер строки> <номер столбца> (пример: 1 1)")
    return flag

# Функция возвращает все диагонали поля (прим. гравная диагональ возвращается дважды)
def diagonals(a, b, c):
    res = []
    for i in range(a, b, c):
        n = 0
        m = i
        tmp1 = []
        tmp2 = []
        while 0 <= n <= height - 1 and 0 <= m <= width - 1:
            tmp1.append(field[n][m])
            tmp2.append(field[m][n])
            n += 1
            m += c
        res.append(tmp1)
        res.append(tmp2)
    return res

# Функция проверки линии (горизонтальной, вертикальной, диагональной) на наличие победной комбинации
def checkLine(line, sign):
    strLine = ''.join(list(map(str, line)))
    return sign * lineSize in strLine

# Функция проверки поля на наличие победной комбинации
def checkField(sign):
    for row in field:
        if checkLine(row, sign):
            return True

    for i in range(width):
        column = [row[i] for row in field]
        if checkLine(column, sign):
            return True

    for diag in diagonals(0, width, 1):
        if checkLine(diag, sign):
            return True

    for diag in diagonals(width - 1, -1, -1):
        if checkLine(diag, sign):
            return True

    return False

# Вспомогательная функция для расчета размера клетки
def cellSize(n):
    if n < 10:
        return 1
    else:
        return 1 + cellSize(n // 10)

# Функция вывода поля на экран
def printField():
    cell = cellSize(max(width, height))
    if cell % 2 == 0:
        cell += 1
    lst = [str(i).rjust(cell,' ') for i in range(1, width+1)]
    header = str("#").rjust(cell,' ') + " |" + '|'.join(lst) + "|"
    print(header)
    for i in range(height):
        row = [j.center(cell, '_') for j in field[i]]
        line = str(i+1).rjust(cell,' ') + " |" + "|".join(row) + "|"
        print(line)
    print("-"*len(header))

# Функция-генератор. Попеременно возвращает информацию о игроках, чей ход предстоит
def gen():
    while True:
        for i in range(len(players)):
            yield i

# Функция, реализующая алгоритм игры
def game():
    print("Игра крестики-нолики")
    while not initField():
        continue
    print("Игрок 1 - X, Игрок 2 - О.\nВведите номер клетки в формате <номер строки> <номер столбца> (пример: 1 1)\nИгра началась!")
    printField()
    for i in gen():
        while not makeMovement(players[i]):
            continue
        printField()
        if checkField(players[i].get('sign')):
            print(players[i].get('name') + " выиграл!")
            break
        if not any('_' in field[row] for row in range(height)):
            print("Поле заполнено. Свободные клетки отсутствуют. Ничья")
            break
    print("Игра окончена")

# Запуск игры
game()

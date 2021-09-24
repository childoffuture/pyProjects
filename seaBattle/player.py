from board import Board
from cell import Cell
import my_exceptions

# Базовый класс игрока
class Player:
    # Конструктор
    def __init__(self, my_board, enemy_board, name):
        self._my_board = my_board
        self._enemy_board = enemy_board
        self._name = name

    # Метод, запрашивающий ход игрока
    def ask(self):
        raise NotImplementedError

    # Метод, реализующий ход игрока
    def move(self):
        result = ""
        while True:
            try:
                cell = self.ask()
                result = self._enemy_board.shot(cell)
            except my_exceptions.BoardOutException as e:
                print(e)
            except my_exceptions.DoubleShootException as e:
                print(e)
            except my_exceptions.InputError as e:
                print(e)
            else:
                break

        return result

    # Вернуть имя игрока
    @property
    def name(self):
        return self._name

    # Вернуть игровое поле игрока
    @property
    def player_board(self):
        return self._my_board

    # Вернуть игровое поле противника
    @property
    def enemy_board(self):
        return self._enemy_board

# Класс игрока-компьютера
class AI(Player):
    # Конструктор
    def __init__(self, my_board, enemy_board):
        super().__init__(my_board, enemy_board, 'Компьютер')

    # Метод, генерирующий ход случайным образом
    def ask(self):
        print()
        print (" Ход компьютера...")
        return Board().random_cell

# Класс игрока-человека
class Human(Player):
    # Конструктор
    def __init__(self, my_board, enemy_board):
        super().__init__(my_board, enemy_board, 'Игрок')

    # Запрос хода в формате буква-цифра + проверка формата
    def ask(self):
        print()
        print(" Формат ввода: <Колонка><Номер строки>")
        command = list(input(" Ваш ход:").upper())
        if len(command) == 2 and command[0] in Board().dict():
            row = int(command[1]) - 1
            column = Board().dict().index(command[0])
            return Cell(row, column)
        else:
            raise my_exceptions.InputError

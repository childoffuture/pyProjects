from os import system
import time
import player
from board import Board
from ship import Ship
import random
import my_exceptions

# Класс, реализующий логику игры
class Game:
    # Конструктор
    def __init__(self):
        self.players = []

    # Функция-генератор игрового поля
    def init_board(self, show_ships):
        ship_sizes = [3,2,2,1,1,1,1]
        board = Board(show_ships)
        for size in ship_sizes:
            attempts = 0
            while True and attempts < 1000:
                try:
                    horizontal = bool(random.randint(0, 1))
                    start_cell = board.random_cell
                    board.add_ship(Ship(start_cell.row, start_cell.column, size, horizontal))
                except my_exceptions.ShipPositionException:
                    attempts += 1
                except my_exceptions.BoardOutException:
                    attempts += 1
                else:
                    break
            if attempts >= 1000:
                raise my_exceptions.InitBoardException
        return board

    # Дополнительный метод, отлавливающий исключения (если доска не смогла сгенериться, перезапускаем процесс)
    def gen_board(self, show_ships):
        board = None
        while True:
            try:
                board = self.init_board(show_ships)
            except my_exceptions.InitBoardException:
                pass
            else:
                break
        return board

    # Запуск игры
    def start(self):
        self.welcome()
        self.init_players()
        self.loop()
        #print("формат ввода: <Колонка><Номер строки> ")

        # make loop
        # in loop make move
        # paint board
        pass

    #   Приветственное сообщение
    def welcome(self):
        print(" -------------------")
        print("   Приветсвуем вас  ")
        print("       в игре       ")
        print("     морской бой    ")
        print(" -------------------")
        input(" Для продолжения нажмите ввод...")
        system('clear')

    # Создание игроков
    def init_players(self):
        ai_board = self.gen_board(False)
        human_board = None
        while True:
            print(" Выберите расстановку кораблей для игры. Введите Y если хотите начать игру с данной расстановкой")
            human_board = self.gen_board(True)
            print(human_board)
            print()
            res = str(input(" Выбрать расстановку? ")).upper()
            system('clear')
            if res == 'Y':
                break

        self.players.append(player.Human(human_board, ai_board))
        self.players.append(player.AI(ai_board, human_board))

    # функция-генератор выбора игрока для хода
    def gen(self):
        while True:
            for pl in self.players:
                yield pl

    # Печать игровых полей в строку
    def print_boards(self, b1, b2):
        b1_lines = str(b1).split('\n')
        b2_lines = str(b2).split('\n')
        for b1_line, b2_line in zip(b1_lines, b2_lines):
            print(b1_line, ' '*5, b2_line)

    # Реализация ходов игрока
    def loop(self):
        for plr in self.gen():
            self.print_boards(self.players[0].player_board, self.players[0].enemy_board)
            if not plr.move():
                time.sleep(1)
                system('clear')
            else:
                print(plr.name, "Выиграл!")
                print("Игра окончена")
                break

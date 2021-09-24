import my_exceptions
import random
from cell import Cell


# Класс игровой доски
class Board:
    # Конструктор
    def __init__(self, show_ships = False):
        self.size = 6
        self.show_flag = show_ships
        self._ships = []
        self.field = [ [" "] * self.size for i in range(self.size) ]

    # Вернуть заголовок поля
    def dict(self):
        return ['A', 'B', 'C', 'D', 'E', 'F']

    # Вернуть рандомную ячейку поля
    @property
    def random_cell(self):
        return Cell(random.randint(0, self.size - 1), random.randint(0, self.size - 1))

    # Печать поля
    #def __repr__(self):
    def __str__(self):
        header = " # | " + " | ".join(self.dict()) + " |"
        line = "-" * (len(header) - 1)
        line = line.rjust(len(line) + 1, ' ')
        result = []
        result.append("")
        result.append(header)

        for i, row in enumerate(self.field):
            result.append(line)
            new_line = str(i+1).rjust(2, ' ') + " | " + " | ".join(row) + " |"
            new_line = new_line.replace("■", " ") if not self.show_flag else new_line
            result.append(new_line)

        return "\n".join(result)

    # Проверка попадания клетки за границы поля
    def out(self, cell):
        return not all(0 <= n < self.size for n in [cell.row, cell.column])

    # Метод добавления корабля
    def add_ship(self, new_ship):
        if any(self.out(cell) for cell in new_ship.cells):
            raise my_exceptions.ShipPositionException

        for existed_ship in self._ships:
            if any(new_cell in existed_ship.cells + existed_ship.contour for new_cell in new_ship.cells):
                raise my_exceptions.ShipPositionException

        self._ships.append(new_ship)
        if self.show_flag:
            for cell in new_ship.cells:
                self.field[cell.row][cell.column] = "■"

    # Возврат флага существования кораблей
    @property
    def ships_exist(self):
        return bool(self._ships)

    # Обработка хода игрока
    def shot(self, cell):
        result = self.dict()[cell.column] + str(cell.row + 1)
        if self.out(cell):
            raise my_exceptions.BoardOutException

        if self.field[cell.row][cell.column] in ['X', 'O']:
            raise my_exceptions.DoubleShootException

        success = False
        for ship in self._ships:
            if cell in ship.cells:
                self.field[cell.row][cell.column] = 'X'
                ship.shot()
                if ship.hp == 0:
                    result += " убит!"
                    self._ships.remove(ship)
                    for contour_cell in ship.contour:
                        if not self.out(contour_cell):
                            self.field[contour_cell.row][contour_cell.column] = 'O'
                else:
                    result += " ранен!"
                success = True
                break

        if not success:
            self.field[cell.row][cell.column] = 'O'
            result += " мимо!"

        return result

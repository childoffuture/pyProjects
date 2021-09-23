from cell import Cell

# Класс корабль
class Ship:
    # Конструктор
    def __init__(self, row, column, size, horizontal=True):
        self.init_cells(row, column, size, horizontal)
        self.init_contour(row, column, size, horizontal)
        self._hp = size

    # Инициализация координат (точек) корабля
    def init_cells(self, row, column, size, horizontal):
        self._cells = []
        for i in range(size):
            if horizontal:
                self._cells.append(Cell(row, column + i))
            else:
                self._cells.append(Cell(row + i, column))

    # Инициализация контура корабля
    def init_contour(self, row, column, size, horizontal):
        self._contour = []
        for i in range(size + 2):
            for j in [-1, 0, 1]:
                cell = None
                if horizontal:
                    cell = Cell(row + j, column - 1 + i)
                else:
                    cell = Cell(row - 1 + i, column + j)
                if cell not in self._cells:
                    self._contour.append(cell)

    # Вывод координат для дебага
    def __repr__(self):
        return str(self.cells)

    # Попадание по кораблю
    def shot(self):
        self._hp -= 1

    # Вернуть 'здоровье' корабля
    @property
    def hp(self):
        return self._hp

    # Вернуть координаты (точки) корабля
    @property
    def cells(self):
        return self._cells

    # Вернуть контур корабля
    @property
    def contour(self):
        return self._contour

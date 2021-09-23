# Класс ячейка (палуба корабля)
class Cell:
    # Конструктор
    def __init__(self, row, column):
        self._row = row
        self._column = column

    # Сравнение ячеек (точек)
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    # Вывод координат для дебага
    def __repr__(self):
        return "(" + str(self.row) + "," + str(self.column) + ")"

    # Вернуть номер строки
    @property
    def row(self):
        return self._row

    # Вернуть номер столбца
    @property
    def column(self):
        return self._column
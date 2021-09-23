# Обрабатываемые исключения
class GameException(BaseException):
    pass

class BoardOutException(GameException):
    def __str__(self):
        return " Клетка за пределами поля"

class ShipPositionException(GameException):
    def __str__(self):
        return " Неверное положение корабля"

class DoubleShootException(GameException):
    def __str__(self):
        return " В эту клетку уже стреляли"

class InitBoardException(GameException):
    def __str__(self):
        return " Не удалось сгенерировать игровое поле"

class InputError(GameException):
    def __str__(self):
        return " Неверный формат команды"

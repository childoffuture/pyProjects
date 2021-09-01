width = 0
height = 0
lineSize = 0
field = []
players = [{'name': 'Player 1', 'sign': 'X'},
           {'name': 'Player 2', 'sign': 'O'}]

def initField():
    flag = False
    global field
    global width
    global height
    global lineSize
    lst = input("enter field params in format <width>x<height>x<linesize> (sample: 3x3x3):").split('x')
    if len(lst) == 3:
        mask = "1234567890"
        if all(i in mask for i in lst[0]):
            if all(i in mask for i in lst[1]):
                if all(i in mask for i in lst[2]):
                    width = int(lst[0])
                    height = int(lst[1])
                    lineSize = int(lst[2])
                    if width >= lineSize or height >= lineSize:
                        print("field size:", width, height)
                        field.clear()
                        for i in range(width):
                            row = []
                            for j in range(height):
                                row.append('_')
                            field.append(row)
                        flag = True
                    else:
                        print("height or width less than lineSize")
            else:
                print("invalid height")
        else:
            print("invalid width")
    else:
        print("invalid format")
    return flag

def makeMovement(player):
    flag = False
    global field
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
                print("cell (%d %d) is not available", row-1, column-1)
        else:
            print("wrong cell number")
    else:
        print("wrong command. Enter cell number in format <row> <column> (sample: 1 1)")
    return flag

def diagonals(a, b, c):
    res = []
    global field
    for i in range(a, b, c):
        lst = []
        n = i
        for row in field:
            if 0 <= n <= width - 1:
                lst.append(row[n])
                n += c
        res.append(lst)
    print (res)
    return res

def checkLine(line, sign):
    strLine = ''.join(list(map(str, line)))
    return sign * lineSize in strLine

def checkField(sign):
    for row in field:
        if checkLine(row, sign):
            return True

    for i in range(width):
        column = [row[i] for row in field]
        if checkLine(column, sign):
            return True

    for diag in diagonals(0, width - 1, 1):
        if checkLine(diag, sign):
            return True

    for diag in diagonals(width - 1, -1, -1):
        if checkLine(diag, sign):
            return True

    return False

def printField():
    lst = [str(i) for i in range(1, width+1)]
    header = "# |" + '|'.join(lst) + "|"
    print(header)
    for i in range(height):
        line = str(i+1) + " |" + "|".join(field[i]) + "|"
        print(line)
    print("-"*len(header))

def gen():
    while True:
        for i in range(len(players)):
            yield i

def game():
    print("this is the game X O")
    while not initField():
        continue
    print("first player - X, second player - O.\nEnter cell number in format <row> <column> (sample: 1 1)\nThe game started!")
    printField()
    for i in gen():
        while not makeMovement(players[i]):
            continue
        printField()
        if checkField(players[i].get('sign')):
            print(players[i].get('name') + " won!")
            break
        if not any('_' in field[row] for row in range(height)):
            print("field is full. No more available cells. It`s a draw")
            break
    print("Game over")

game()

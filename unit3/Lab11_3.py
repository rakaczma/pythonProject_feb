import random

BLANK_SQUARE = "--"
pieces = ["WP", "BP", "BP", "BT", "WQ"]

chessboard = [[BLANK_SQUARE for i in range(8)] for i in range(8)]

counter = 0
while counter < 5:
    row = random.randint(0, 7)
    column = random.randint(0, 7)
    if chessboard[row][column] == BLANK_SQUARE:
        chessboard[row][column] = pieces[counter]
        counter += 1

for row in range(len(chessboard)):
    if row == 0:
        print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep="  ")
    print(row + 1, end=" ")
    for column in range(len(chessboard[row])):
        print(chessboard[row][column], end=" ")
    print()
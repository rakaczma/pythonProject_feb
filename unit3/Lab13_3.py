import random

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5

def draw_letter():
    # return chr(random.randint(ord("A"), ord("C")))
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))


def draw_row():
    # return [draw_letter() for i in range(3)]
    return [draw_letter() for i in range(NUMBER_OF_LETTERS)]

def check(row):
    first_element = row[0]
    for element in row:
        if element != first_element:
            return False
    return True
    # if row[0] == row[1] and row[1] == row[2]:
    #     return True
    # else:
    #     return False


counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1


# import random
#
# wyniki = []
# #rzut = 0
# for i in range(1, 17):
#     wynik = random.randint(1, 6)
#     wyniki.append(wynik)
#  #   rzut = 8
# print(wyniki)
# print(wyniki[7])

import random

dice_rolls_total = 16
rolls = []

for i in range(dice_rolls_total):
    rolls.append(random.randint(1, 6))

print("Zbiór wyników po", dice_rolls_total, "rzutach kostką do gry:", rolls)
print("Za 8 razem wyrzucono wartość", str(rolls[8 - 1]) + ".")

sixes_total = 0  # zaczynamy 6 od zera
for roll in rolls: # rzuty
    if roll == 6: # jesli wyrzuci 6 to..
        sixes_total += 1 # zlicza wyrzucone 6
print("Wyrzucono", sixes_total, "razy szóstkę.")

in_row_value_tmp = rolls[0]
in_row_total_tmp = 0
in_row_value = 0
in_row_total = 0

for roll in rolls:
    if (roll == in_row_value_tmp):
        in_row_total_tmp += 1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_total = in_row_value_tmp
print("Pod rząd wyrzucono", in_row_total, "razy wartość", str(in_row_value) + ".")
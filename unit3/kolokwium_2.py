# Napisz skrypt tworzący i wyświetlający listę liczb całkowitych z zakresu podanego przez użytkownika.
# Przykładowo dla podanych liczb 1 i 5 na ekranie powinno się pojawić [1, 2, 3, 4, 5].

import random

od_liczby = int(input("Podaj początkową liczbe zakresu: "))
do_liczby = int(input("Podaj końcowa liczbe zakresu: "))

user_numbers = []

for i in range(od_liczby, do_liczby + 1):
    user_numbers.append(i)

print(user_numbers)


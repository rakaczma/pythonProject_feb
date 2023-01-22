# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

od_liczby = int(input("Podaj początkową liczbe zakresu: "))
do_liczby = int(input("Podaj końcowa liczbe zakresu: "))

for i in range(od_liczby, do_liczby + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
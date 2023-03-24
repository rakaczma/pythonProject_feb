# 3. Napisz grę polegającą na zapamiętywaniu kolejnych słów. Wylosowany
# gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
# Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej
# samej kolejności i także dodać swoje. Rozgrywka kończy się gdy, któryś z
# graczy popełni błąd. Na ekranie komputera przy każdej turze należy
# wymazać ekran np. przez wyświetlenie 100 pustych wierszy.


current_word = input("Elo! Grę zaczynamy od słowa: ")
words = [current_word]

while True:
    print("Aktualne słowo: ", current_word)
    player_word = input("Podaj kolejne słowo: ")
    if player_word == "koniec":
        break
    elif player_word not in words and player_word != "":
        words.append(player_word)
        current_word = player_word
    else:
        print("Nieprawidłowe słowo! Koniec gry!")
        break
    print("Twoje słowa:", words)

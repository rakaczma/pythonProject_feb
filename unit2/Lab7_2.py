number = int(input("Podaj liczbę punktów: "))

if number >= 95:
    print("Ocena bardzo dobra 5,0.")
elif number < 95 and number > 84:
    print("Ocena dobra 4,5.")
elif number > 60 and number < 70:
    print("Ocena dość dobra 3,5.")
elif number <= 60 and number > 50:
    print("Ocena dostateczna 3,0.")
else:
    print("Ocena niedostateczna.")
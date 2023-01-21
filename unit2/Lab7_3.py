import random

number = random.randint(1, 10)
msg = "Zgadnij jaka liczbe od 1 do 10 mam na myśli! "
guess = int(input(msg))
if guess == number:
    print("Brawo! To mialem na mysli!")
else:
    msg = "Masz kolejną szansę, ... "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
            msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało się odgadnąć za drugim razem!")
    else:
        msg = "Masz kolejna szansę, moja liczba jest "
        if number > 5:
            msg += "większa  "
        else:
            msg += "mniejsza lub równa "
            msg += "od liczby 5: "
        guess = int(input(msg))
    if guess == number:
        print("Brawo! Do trzech razy sztuka")
    else:
        msg = "niestety myslalem o liczbie " + str(number) + "."
        print(msg)

    #print("niestety myslalem o liczbie " + str(number) + ".")

#print(number)


import random

counter = 1
number = random.randint(1, 10)
guess = int(input("Zgadnij jaka liczba od 1 do 10!"))

while number != guess:
    guess = int(input("To nie ta, spróbuj jeszcze raz:"))
    counter += 1

print("Brawo, udało Ci sie za " + str(counter) + " razem.")
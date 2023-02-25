numbers = []
numbers_total = int(input("Podaj liczbę elementów zbioru: "))

for i in range(numbers_total):
    number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
    numbers.append(number)

numbers.sort(reverse=True)

numbers_without_duplicates = []
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)

print(numbers_without_duplicates)
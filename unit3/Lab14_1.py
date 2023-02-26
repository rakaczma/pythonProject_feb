# phones = {"Tomek": 123456789, "Ada": 234567890, "Karol": 321654987}
#
# name = input("Podaj imię: ")
#
# if name in phones:
#     print(phones.get(name))
# else:
#     print("Brak numeru!")
#

phones = {
    "Adam": 123123123,
    "Karol": 112112113,
    "Mariola": 132465789,
    "Iza": 456743124
}

while True:
    name = input("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("Telefon: ", phones[name])
    else:
        print("Nie znaleziono telfonu dla imienia:", name)
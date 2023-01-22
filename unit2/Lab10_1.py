names = []

names_qty = int(input("Powiedz ile imion!"))

for i in range(names_qty):
    name = input("Powiedz imię!")
    names.append(name)
print("Podane imiona to: ", names)
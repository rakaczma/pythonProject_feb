# szachownica ma 64 pola

# 0 1 2 3 4
# 1 2 4 8 16 .... 2 ** 1
sum = 0
for i in range(64):
    sum += 2 ** i
print("Suma wszystkich ziaren na szachownicy: " + str(sum))

# 1 ziarno - 0,4 mg
# 1 ziarno - 0,0004 g

tons = int(sum * 0.0004 / 1000 / 1000)
print(tons)

# produkcja pszenicy na świecie to ok. 782mln ton
years = round(tons / 782e6, 2)
print(years)

# pociąg może transportować 2200t
trains = round(tons / 2200, 1)
print(trains)
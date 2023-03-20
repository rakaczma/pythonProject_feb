# 2. Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy
# wyższy poziom wymaga jednej puszki mniej niż poziom na którym go
# zbudowano. Korzystając z rekurencji napisz program, który pozwoli
# wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym
# poziomie oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z
# dostępnej liczby puszek. Przykład: jeżeli chcemy ułożyć 3 poziomową
# wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4
# poziomową wieżę.


levels = int (input("Podaj ilość poziomów: "))

def pyramide_by_levels(levels):
  if (levels == 0):
    return 0
  else:
    return levels + pyramide_by_levels(levels - 1)

print("Piramida będzie składać się z", pyramide_by_levels(levels), "puszek.", end="\n")

cans = int (input("Podaj ilość puszek: "))

def pyramide_by_cans(cans):
    if (cans == 0):
        return 0
    else:
        return cans - pyramide_by_cans(cans - 1)

print("Piramida będzie składać się z", pyramide_by_cans(cans), "poziomów.")
# 2. Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
# 2, 'r': 2, 'c': 1, 'd': 1 }.

# lista  l = [1, 2, 3]  l[0] - list
# krotka t = (1, 2, 3)  t[1] - tuple
# słownik d = {"a": 1, "b": 2} - dict
# ciąg znaków s = "abcde" - str

def count_letters(string):
    stats = {}
    for char in string:
        if char in stats.keys():  # czy występuje juz ten klucz w słowniku
            stats[char] += 1
        else:
            stats[char] = 1
    return stats


print(count_letters("abracadabra"))


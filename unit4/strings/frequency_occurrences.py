# napisz funkcję zliczającą ilość wystąpień poszczególnych elementów listy w formie słownika.
# Przykład:
# print(frequency_occurences(["Ala", "Tomek", "Ala"]))
#
# {'Ala': 2, 'Tomek: 1'}

def frequency_occurences(source_list):
    target_dict = {}
    for e in source_list:
        # target_dict[e] = source_list.count(e)
        if e in target_dict:
            target_dict[e] += 1
        else:
            target_dict[e] = 1
    return target_dict

print(frequency_occurences(["Ala", "Tomek", "Ala"]))
print(frequency_occurences([1, 1, 1]))
# Napisz funkcję usuwającą duplikaty z dowolnej listy elementów.
#
# Przykład:
#
# print(remove_duplicates(["Ala", "Zosia", "Zosia", "Marek"]))
#
# ["Ala", "Zosia", "Marek"]

def remove_duplicates(list):
    list = ["Kiwior", "Bednarek", "Kiwior", "Lewandowski", "Szczęsny", "Lewandowski"]

    no_duplicates_list = []
    for name in list:
        if name not in no_duplicates_list:
            no_duplicates_list.append(name)

    print(no_duplicates_list)

remove_duplicates(list)
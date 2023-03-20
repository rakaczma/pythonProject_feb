# 1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

def remove_duplicates():
    list = [2, 45, 3, 2, 6, 101, 5, 2, 13]

    no_duplicates_list = []
    for number in list:
        if number not in no_duplicates_list:
            no_duplicates_list.append(number)

    print(no_duplicates_list)

remove_duplicates()
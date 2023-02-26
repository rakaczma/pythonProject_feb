def merge_list_without_duplicates(source, target):
    for e in source:
        if e not in target:
            target.append(e)

def transform_data(list1, list2, list3):
    result = []
    merge_list_without_duplicates(list1, result)
    merge_list_without_duplicates(list2, result)
    merge_list_without_duplicates(list3, result)
    return tuple(result)


print(transform_data([1, 2], [1, 1], [4, 4, 4]))
print(transform_data([1, 2, 3], [1, 2, 3], [4, 5, 6]))
print(transform_data(["Ala", "ma"], ["Ala", "ma", "kota"], ["mysz"]))
"""This is module for Lab16_2..."""

def is_int(item):
    """Intiger value validator"""
    return all([isinstance(item, int) for item in list])

def sum_all_elem(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def multiplicate_all_elem(list):
    multiplication = 1
    for i in list:
        multiplication *= i
    return multiplication


if __name__ == "__main__":
    print(is_int([1, 3.4, 4]) == False)
    print(is_int([6, 54, 13]) == True)
    print(sum_all_elem([2, 1, 3]) == 6)
    print(sum_all_elem([5, 2, 4]) == 11)
    print(multiplicate_all_elem([2, 1, 3]) == 6)
    print(multiplicate_all_elem([3, 7, 2]) == 42)
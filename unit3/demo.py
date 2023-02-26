# def sum_numbers(numbers):
#     sum = 0
#     for element in numbers:
#         sum += element
#     return sum
#
# numbers = [1, 2, 3]
# result = sum_numbers(numbers)
# print(result)
#
#
# def scope_test():
#     global x
#     x = 123
#     print("w srodku funkcji: " + str(x))
#
# x = 99
# scope_test()
# print("na zewnątrz: " + str(x))

# def change_value(n):
#     print("przed zmianą: ", n)
#     n[0] = 999
#     print("po zmianie: ", n)
#
# val = [1, 2]
# change_value(val)
# print(val)

def my_func(*args):
    for el in args:
        print(el)

my_func(1,2,3,4,5)
# numbers = (1, 2, 3)
# numbers = 1, 2, 3
# numbers = ()

#numbers = (1,)

# for i in numbers:
#     print(i)

numbers = tuple(x for x in range(10))

print(numbers)

numbers[0] = 9999
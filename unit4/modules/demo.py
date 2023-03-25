# import math
# import sys

# print(math.pi)
# print(math.sin(math.pi / 2))
# print(math.factorial(5)) # 1 * 2 * 3 * 4 * 5
# print(math.floor(4.99999))

# from math import pi, sin, factorial
# print(pi)
# print(sin(pi / 2))
# print(factorial(8))

# import math as m
#
# print(m.pi)

# from math import pi as mathpi
#
# print(mathpi)

# import math
#
# # print(dir(math))
# for e in dir(math):
#     print(e)

# import random

# for e in dir(random):
#     print(e)

# print(random.randint(1, 3))
# print(random.random())

# from random import random, seed
#
# seed(0)
#
# for i in range(5):
#     print(random())

# from random import choice, sample
#
# # lst = [1,2,3,4,5,6,7,8,9,10]
# lst = [i for i in range(1, 11)]
#
# print(choice(lst))
# print(sample(lst, 5))

# import platform
#
# # help(platform)
#
# print(platform.machine())
# print(platform.processor())
# print(platform.system())
# print(platform.version())
# print(platform.python_implementation())
# print(platform.python_version_tuple())

# from platform import machine, version
#
# help(machine)
# print(machine())
# help(version)
# print(version())

from platform import platform

help(platform)
print(platform(True, True))
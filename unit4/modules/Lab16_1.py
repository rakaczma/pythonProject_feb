import platform
import random
import math

print("Procesor: ", platform.processor())

numbers = [i for i in range(1, 11)]
print("Losowanie:", random.sample(numbers, 3))

print("Sinus 90 stopni: ", math.sin(math.radians(90)))



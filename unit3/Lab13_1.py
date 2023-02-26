def pow(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers

print(pow([1, 2, 3], 2))

def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result

print(pow2([1, 2, 3], 2))

def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]

print(pow3([1, 2, 3], 2))
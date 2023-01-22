digits = [1, 2, 4, 6, 6, 2, 6, 6, 9, 7]
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digit in digits:
    frequency[digit] += 1

print(frequency)

most_common = -1
for i in range(len(frequency)):
    if frequency[i] > most_common:
        most_common = i

print("najczęściej występującą cyfrą jest " + str(most_common) + ",", "występuje", frequency[most_common], "razy.")
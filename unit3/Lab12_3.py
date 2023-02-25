def calculate_bmi(weight_in_kg, height_in_cm):
    return weight_in_kg / height_in_cm ** 2


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


print("Obliczanie wskaźnika BMI!")
weight_in_kg = float(input("Podaj swoją wagę w kg: "))
height_in_cm = float(input("Podaj swój wzrost w cm: "))

bmi = calculate_bmi(weight_in_kg, height_in_cm * 0.01)
category = determine_bmi_category(bmi)

print("Wskaźnik BMI:", bmi)
print("Kategoria: ", category)

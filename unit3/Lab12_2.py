def perimeter(a, b):
    return 2 * a + 2 * b

def surface_area(a, b):
    return a * b

def diagonal_length(a, b):
    return (a ** 2 + b ** 2) ** (1 / 2)

def show_result(a, b):
    print("Prostokąt o bokach ", a, "i", b)
    print("Obwód:", perimeter(a, b))
    print("Pole powierzchni:", surface_area(a, b))
    print("Długość przekątnej:", diagonal_length(a, b))
    print()

show_result(4, 5)
show_result(2678, 5678)
show_result(344555, 788998)
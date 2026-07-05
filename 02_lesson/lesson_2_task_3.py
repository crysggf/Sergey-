import math


def square(side):
    area = side * side
    if not side.is_integer():
        area = math.ceil(area)
    return area


result = square(2.3)
print(f'Площадь квадрата со стороной 2.3: {result}')

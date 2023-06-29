import math


def square():
    side_of_a_square = float(input("Введите сторону квадрата в цифрах >>> "))
    square_area = side_of_a_square * side_of_a_square
    square_area = math.ceil(square_area)
    print(square_area)


square()

import math


def get_triangle_area_by_heron(base_length, first_side_length, second_side_length) -> float:
    if base_length == 0 or first_side_length == 0 or second_side_length == 0:
        return 0.0
    semi_perimeter = (base_length + first_side_length + second_side_length) / 2
    under_root_expression = semi_perimeter * (semi_perimeter - base_length) * (semi_perimeter - first_side_length)\
        * (semi_perimeter - second_side_length)
    return math.sqrt(under_root_expression)


if __name__ == '__main__':
    print(get_triangle_area_by_heron(int(input("Enter length of base ")), int(input("Enter length of first side ")),
                                     int(input("Enter length of second side "))))

def get_shape_with_area(shape_name) -> dict:
    if shape_name == "triangle":
        base_length = int(input("Enter base of triangle "))
        height_length = int(input("Enter height of triangle "))
        return {shape_name: (base_length * height_length) / 2}
    if shape_name == "rectangle":
        first_side_length = int(input("Enter length of rectangle "))
        second_side_length = int(input("Enter width of rectangle "))
        return {shape_name: first_side_length * second_side_length}
    if shape_name == "circle":
        radius_length = int(input("Enter radius of circle "))
        return {shape_name: 3.14 * (radius_length ** 2)}


if __name__ == '__main__':
    for shape, area in get_shape_with_area(str(input("Enter shape name "))).items():
        print("{'", shape, "': ", area, "}")


import numpy


def convert_matrix_to_vector(matrix) -> list:
    vector = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            vector.append(matrix[row][column])
    return vector


if __name__ == '__main__':
    matrix_to_convert = numpy.random.rand(3, 3)
    print("Initial matrix:")
    print(matrix_to_convert, "\n")
    print("Vector: ", convert_matrix_to_vector(matrix_to_convert))

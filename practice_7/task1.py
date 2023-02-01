import numpy


if __name__ == '__main__':
    first_array = numpy.array([80, 98, 75, 91, 78])
    second_array = numpy.array([100, 82, 105, 89, 102])
    correlation_coefficient = numpy.corrcoef(first_array, second_array)[0, 1]
    print("Correlation: ", correlation_coefficient)

import numpy
import matplotlib.pyplot


if __name__ == '__main__':
    first_array = numpy.array([80, 98, 75, 91, 78])
    second_array = numpy.array([100, 82, 105, 89, 102])

    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.scatter(first_array, second_array, color='crimson', label='dots')
    matplotlib.pyplot.title('Scatterplot: ', fontsize=20)
    matplotlib.pyplot.xlabel('X axis')
    matplotlib.pyplot.ylabel('Y axis')
    matplotlib.pyplot.show()
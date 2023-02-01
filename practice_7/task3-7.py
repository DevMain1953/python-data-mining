import numpy
import matplotlib.pyplot
import pandas
from sklearn.linear_model import LinearRegression


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('bitcoin.csv')
    projection = 14
    data_from_csv_file['predict'] = data_from_csv_file['close'].shift(-projection)
    x_dataframe = pandas.DataFrame(data_from_csv_file, columns=['close'])
    y_dataframe = pandas.DataFrame(data_from_csv_file, columns=['predict'])
    x_array = numpy.array(x_dataframe, type(float))
    y_array = numpy.array(y_dataframe, type(float))

    x_array = x_array[:-projection]
    y_array = y_array[:-projection]

    matplotlib.pyplot.scatter(x_array, y_array, color='m', marker='o', s=30)
    matplotlib.pyplot.xlabel('X axis')
    matplotlib.pyplot.ylabel('Y axis')

    linear_regression = LinearRegression()
    linear_regression.fit(x_array, y_array)

    matplotlib.pyplot.plot(x_array, linear_regression.predict(x_array), color='g')
    matplotlib.pyplot.show()

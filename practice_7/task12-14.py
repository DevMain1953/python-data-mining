import numpy
import pandas
import matplotlib.pyplot


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def get_line_of_prediction_from_two_arrays(x_array, y_array):
    size_of_x_array = numpy.size(x_array)
    first_temporary_value = (numpy.sum(x_array * y_array) - size_of_x_array * numpy.mean(y_array) * numpy.mean(x_array)
                             / numpy.sum(x_array * x_array) - size_of_x_array * numpy.mean(x_array) * numpy.mean(x_array))
    second_temporary_value = numpy.mean(y_array) - first_temporary_value * numpy.mean(x_array)
    return second_temporary_value + first_temporary_value * x_array


if __name__ == '__main__':
    data_from_csv_file = read_data_from('housePrice.csv')
    data_from_csv_file['Address'].fillna('other', inplace=True)

    for column_name in data_from_csv_file.columns:
        missing_value = numpy.mean(data_from_csv_file[column_name].isna() * 100)

    data_from_csv_file['Area'] = pandas.to_numeric(data_from_csv_file['Area'], errors='coerce')
    data_from_csv_file['Price(USD)'] = pandas.to_numeric(data_from_csv_file['Price(USD)'], errors='coerce')
    data_from_csv_file['Area'].fillna(data_from_csv_file['Area'].median(), inplace=True)
    x_dataframe = pandas.DataFrame(data_from_csv_file, columns=['Area'])
    y_dataframe = pandas.DataFrame(data_from_csv_file, columns=['Price(USD)'])
    x_array = numpy.array(x_dataframe, type(float))
    y_array = numpy.array(y_dataframe, type(float))

    matplotlib.pyplot.scatter(x_array, y_array, color='m', marker='o', s=30)
    matplotlib.pyplot.plot(x_array, get_line_of_prediction_from_two_arrays(x_array, y_array), color='g', alpha=0.5)
    matplotlib.pyplot.xlabel('X axis')
    matplotlib.pyplot.ylabel('Y axis')
    matplotlib.pyplot.show()

import numpy
import pandas
from sklearn.linear_model import LinearRegression


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


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

    linear_regression = LinearRegression()
    linear_regression.fit(x_array, y_array)

    print("Slope of the regression line: ", linear_regression.coef_)
    print("Y-interception: ", linear_regression.intercept_)

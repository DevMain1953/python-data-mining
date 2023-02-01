import pandas
import matplotlib.pyplot


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def display_window_with_boxplot_using(data_from_csv_file):
    matplotlib.pyplot.figure(figsize=(100, 8))
    matplotlib.pyplot.boxplot([data_from_csv_file['bmi'], data_from_csv_file['age'], data_from_csv_file['children'],
                               data_from_csv_file['charges']], labels=['bmi', 'age', 'children', 'charges'], vert=False)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    display_window_with_boxplot_using(read_data_from('insurance.csv'))

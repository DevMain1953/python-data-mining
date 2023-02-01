import pandas


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def generate_descriptive_statistics_from(dataframe):
    return dataframe.describe()


if __name__ == '__main__':
    print(generate_descriptive_statistics_from((read_data_from('insurance.csv'))))

import pandas


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('insurance.csv')
    print(data_from_csv_file.loc[data_from_csv_file.duplicated()])
    data_without_duplicates = data_from_csv_file.drop_duplicates()

import pandas


def read_data_from(url_to_csv):
    return pandas.read_csv(url_to_csv)


def call_info_method_on(dataframe):
    dataframe.info()


def get_first_rows_from(dataframe):
    return dataframe.head()


def get_sum_of_empty_values_in(dataframe):
    return dataframe.isna().sum()


if __name__ == '__main__':
    csv_data = read_data_from("https://query1.finance.yahoo.com/v7/finance/download/GE?period1=-252374400&period2="
                              "1663718400&interval=1d&events=history&includeAdjustedClose=true")

    print("\nInformation about data from csv file:")
    call_info_method_on(csv_data)
    print("\nHead of data from csv file:")
    print(get_first_rows_from(csv_data))
    print("\nEmpty values in data from csv file:")
    print(get_sum_of_empty_values_in(csv_data))

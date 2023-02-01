import pandas


def read_data_from(url_to_csv):
    return pandas.read_csv(url_to_csv)


if __name__ == '__main__':
    csv_data = read_data_from("https://query1.finance.yahoo.com/v7/finance/download/GE?period1=-252374400&period2="
                              "1663718400&interval=1d&events=history&includeAdjustedClose=true")
    print(csv_data)

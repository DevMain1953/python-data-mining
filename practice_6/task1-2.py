import numpy
import pandas


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def print_dataframe_with_removed_two_features_and_filled_skips_in(dataframe):
    dataframe.drop(['geoId', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'], axis=1, inplace=True)
    dataframe['countryterritoryCode'].fillna('other', inplace=True)
    dataframe['popData2019'].fillna(dataframe['popData2019'].median(), inplace=True)
    for column_name in dataframe.columns:
        print(column_name + ": " + str(numpy.mean(dataframe[column_name].isna() * 100)))


def print_descriptive_statistics_from(dataframe):
    print(dataframe.describe())


def print_countries_and_days_where_number_of_deaths_is_more_than_3000_from(dataframe):
    print(dataframe.loc[dataframe['deaths'] > 3000, ['countriesAndTerritories', 'day']])


def remove_duplicates_from(dataframe):
    return dataframe.drop_duplicates()


if __name__ == '__main__':
    data_from_csv_file = read_data_from('ECDCCases.csv')
    print(data_from_csv_file.loc[data_from_csv_file.duplicated()])
    dataframe_with_removed_duplicates = remove_duplicates_from(data_from_csv_file)
    print(dataframe_with_removed_duplicates)

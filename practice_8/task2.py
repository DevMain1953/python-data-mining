from scipy.stats import f_oneway
import pandas


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('insurance.csv')
    data_without_duplicates = data_from_csv_file.drop_duplicates()
    dataframe = pandas.DataFrame({'region': data_without_duplicates['region'], 'bmi': data_without_duplicates['bmi']})
    groups = dataframe.groupby('region').groups

    southwest = dataframe['bmi'][groups['southwest']]
    northwest = dataframe['bmi'][groups['northwest']]
    southeast = dataframe['bmi'][groups['southeast']]
    northeast = dataframe['bmi'][groups['northeast']]
    result_of_anova_test = f_oneway(southwest, northwest, southeast, northeast)
    print(result_of_anova_test)

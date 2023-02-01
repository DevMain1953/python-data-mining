from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas
import matplotlib.pyplot


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('insurance.csv')
    data_without_duplicates = data_from_csv_file.drop_duplicates()
    data_without_duplicates['combination'] = data_without_duplicates['region'] + ' / ' + data_without_duplicates['sex']
    result_of_tukey_test = pairwise_tukeyhsd(endog=data_without_duplicates['bmi'],
                                             groups=data_without_duplicates['combination'], alpha=0.95)
    result_of_tukey_test.plot_simultaneous()
    result_of_tukey_test.summary()
    matplotlib.pyplot.show()

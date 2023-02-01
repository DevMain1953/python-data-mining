from scipy.stats import ttest_ind as perform_t_test_for_average_value_of_two_independent_samples
from scipy.stats import shapiro as perform_shapiro_wilk_test_for_normality
from scipy.stats import bartlett as perform_test_of_bartlett_for_equal_variances

import pandas


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('bmi.csv')
    first_data_set = data_from_csv_file.loc[data_from_csv_file['region'] == 'northwest']
    first_data_set_converted_to_list = first_data_set['bmi'].tolist()
    second_data_set = data_from_csv_file.loc[data_from_csv_file['region'] == 'southwest']
    second_data_set_converted_to_list = second_data_set['bmi'].tolist()
    result_of_t_test = perform_t_test_for_average_value_of_two_independent_samples(first_data_set_converted_to_list,
                                                                        second_data_set_converted_to_list)
    first_result_of_shapiro_wilk_test = perform_shapiro_wilk_test_for_normality(first_data_set_converted_to_list)
    second_result_of_shapiro_wilk_test = perform_shapiro_wilk_test_for_normality(second_data_set_converted_to_list)
    result_of_test_of_bartlett = perform_test_of_bartlett_for_equal_variances(first_data_set_converted_to_list,
                                                                          second_data_set_converted_to_list)
    print("Student's criterion: ", result_of_t_test)
    print("Results of Shapiro's tests: ", first_result_of_shapiro_wilk_test, ", ",  second_result_of_shapiro_wilk_test)
    print("Barlett's criterion: ", result_of_test_of_bartlett)
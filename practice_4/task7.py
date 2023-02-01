import pandas
from numpy import mean as get_average_value_from
from scipy.stats import sem as get_standard_error_of_average_value_from
from scipy.stats import t as continuous_random_variable_of_student


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def get_confidence_interval(confidence, df, location, scale):
    return continuous_random_variable_of_student.interval(confidence=confidence, df=df, loc=location, scale=scale)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('insurance.csv')
    print("bmi 0.95 confidence interval is ",
          get_confidence_interval(0.95,
                                  len(data_from_csv_file['bmi']) - 1,
                                  get_average_value_from(data_from_csv_file['bmi']),
                                  get_standard_error_of_average_value_from(data_from_csv_file['bmi'])))
    print("bmi 0.99 confidence interval is ",
          get_confidence_interval(0.99,
                                  len(data_from_csv_file['bmi']) - 1,
                                  get_average_value_from(data_from_csv_file['bmi']),
                                  get_standard_error_of_average_value_from(data_from_csv_file['bmi'])))
    print("charges 0.95 confidence interval is ",
          get_confidence_interval(0.95,
                                  len(data_from_csv_file['bmi']) - 1,
                                  get_average_value_from(data_from_csv_file['charges']),
                                  get_standard_error_of_average_value_from(data_from_csv_file['bmi'])))
    print("charges 0.99 confidence interval is ",
          get_confidence_interval(0.99,
                                  len(data_from_csv_file['bmi']) - 1,
                                  get_average_value_from(data_from_csv_file['charges']),
                                  get_standard_error_of_average_value_from(data_from_csv_file['bmi'])))

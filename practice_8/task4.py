import numpy
import pandas
from scipy.stats import ttest_ind


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('insurance.csv')
    data_without_duplicates = data_from_csv_file.drop_duplicates()
    groups = data_without_duplicates.groupby('region').groups

    pairs = []
    array_with_unique_elements = numpy.array(data_without_duplicates.region.unique())
    for region in range(3):
        for subregion in range(region + 1, 4):
            pairs.append((array_with_unique_elements[region], array_with_unique_elements[subregion]))

    for region, subregion in pairs:
        print(region, subregion)
        print(ttest_ind(data_without_duplicates['bmi'][groups[region]],
                        data_without_duplicates['bmi'][groups[subregion]]))

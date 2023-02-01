import pandas
import matplotlib.pyplot
from sklearn.cluster import DBSCAN
import seaborn
import time


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def get_current_time():
    return time.time()


if __name__ == '__main__':
    data_from_csv_file = read_data_from('Mall_Customers.csv').drop_duplicates()
    data_from_csv_file.Gender.replace({'Male': 1, 'Female': 0}, inplace=True)
    data_from_csv_file.drop('CustomerID', axis=1, inplace=True)

    model = DBSCAN(eps=11, min_samples=5).fit(data_from_csv_file)
    labels = model.labels_

    data_from_csv_file['Claster'] = labels
    start_of_time_range = get_current_time()
    seaborn.scatterplot(x=data_from_csv_file['Age'], y=data_from_csv_file['Annual Income (k$)'],
                        hue=data_from_csv_file['Claster'], data=data_from_csv_file, palette='bright')
    matplotlib.pyplot.show()
    print("Time of DBSCAN: ", format(get_current_time() - start_of_time_range))

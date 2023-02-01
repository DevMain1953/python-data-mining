import pandas
import matplotlib.pyplot
import numpy
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
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
    for column_name in data_from_csv_file.columns:
        missing_value = numpy.mean(data_from_csv_file[column_name].isna() * 100)
    models = []
    values_of_cost_function = []
    values_of_silhouette_coefficient = []
    for i in range(2, 10):
        model = KMeans(n_clusters=i, random_state=123, init='k-means++').fit(data_from_csv_file)
        models.append(model)
        values_of_cost_function.append(model.inertia_)
        values_of_silhouette_coefficient.append(silhouette_score(data_from_csv_file, model.labels_))

    matplotlib.pyplot.grid()
    matplotlib.pyplot.plot(numpy.arange(2, 10), values_of_cost_function, marker='o')
    matplotlib.pyplot.show()
    matplotlib.pyplot.grid()
    matplotlib.pyplot.plot(numpy.arange(2, 10), values_of_silhouette_coefficient, marker='o')
    matplotlib.pyplot.show()

    other_model = KMeans(n_clusters=9, random_state=123, init='k-means++').fit(data_from_csv_file)
    print(other_model.cluster_centers_)
    labels = other_model.labels_

    data_from_csv_file['Claster'] = labels
    start_of_time_range = get_current_time()
    print(data_from_csv_file['Claster'].value_counts())
    figure = matplotlib.pyplot.figure()
    seaborn.scatterplot(x=data_from_csv_file['Age'], y=data_from_csv_file['Annual Income (k$)'],
                        hue=data_from_csv_file['Claster'], data=data_from_csv_file, palette='bright')
    matplotlib.pyplot.show()
    print("Time of k-means: ", format(get_current_time() - start_of_time_range))

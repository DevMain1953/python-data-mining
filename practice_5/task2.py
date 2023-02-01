import pandas
import matplotlib.pyplot
# you need to install umap-lern to make umap.UMAP() available
import umap
import time
from sklearn import preprocessing


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def get_dataframe_from(data_from_csv_file):
    return pandas.DataFrame(data_from_csv_file)


def get_normalized_dataframe_from(denormalized_dataframe):
    return pandas.DataFrame(preprocessing.MinMaxScaler().fit_transform(denormalized_dataframe),
                            columns=denormalized_dataframe.columns)


def get_current_time():
    return time.time()


def visualize_dataframe_using_umap(dataframe):
    new_dataframe = dataframe.drop(['CustomerID', 'Gender'], axis=1)
    normalized_dataframe = get_normalized_dataframe_from(new_dataframe)
    copy_of_normalized_dataframe = normalized_dataframe.copy()

    first_transformed_umap_array = umap.UMAP(n_neighbors=5, min_dist=0.1,
                                             metric='correlation').fit_transform(copy_of_normalized_dataframe)
    start_of_first_time_range = get_current_time()
    second_transformed_umap_array = umap.UMAP(n_neighbors=25, min_dist=0.1,
                                              metric='correlation').fit_transform(copy_of_normalized_dataframe)
    start_of_second_time_range = get_current_time()
    third_transformed_umap_array = umap.UMAP(n_neighbors=50, min_dist=0.1,
                                             metric='correlation').fit_transform(copy_of_normalized_dataframe)
    start_of_third_time_range = get_current_time()
    fourth_transformed_umap_array = umap.UMAP(n_neighbors=5, min_dist=0.6,
                                              metric='correlation').fit_transform(copy_of_normalized_dataframe)
    start_of_fourth_time_range = get_current_time()
    fifth_transformed_umap_array = umap.UMAP(n_neighbors=25, min_dist=0.6,
                                             metric='correlation').fit_transform(copy_of_normalized_dataframe)
    start_of_fifth_time_range = get_current_time()
    sixth_transformed_umap_array = umap.UMAP(n_neighbors=50, min_dist=0.6,
                                             metric='correlation').fit_transform(copy_of_normalized_dataframe)
    start_of_sixth_time_range = get_current_time()

    figure, axes = matplotlib.pyplot.subplots(1, 3, figsize=(15, 4))
    axes[0].scatter(first_transformed_umap_array[:, 0], first_transformed_umap_array[:, 1],
                    c=copy_of_normalized_dataframe.iloc[:, 0], cmap='tab10')
    axes[1].scatter(second_transformed_umap_array[:, 0], second_transformed_umap_array[:, 1],
                    c=copy_of_normalized_dataframe.iloc[:, 0], cmap='tab10')
    axes[2].scatter(third_transformed_umap_array[:, 0], third_transformed_umap_array[:, 1],
                    c=copy_of_normalized_dataframe.iloc[:, 0], cmap='tab10')
    axes[0].set_title("n_neighbors=5, min_dist=0.1", color='black', fontsize=16)
    axes[1].set_title("n_neighbors=25, min_dist=0.1", color='black', fontsize=16)
    axes[2].set_title("n_neighbors=50, min_dist=0.1", color='black', fontsize=16)

    figure, remaining_axes = matplotlib.pyplot.subplots(1, 3, figsize=(15, 4))
    remaining_axes[0].scatter(fourth_transformed_umap_array[:, 0], fourth_transformed_umap_array[:, 1],
                              c=copy_of_normalized_dataframe.iloc[:, 0], cmap='tab10')
    remaining_axes[1].scatter(fifth_transformed_umap_array[:, 0], fifth_transformed_umap_array[:, 1],
                              c=copy_of_normalized_dataframe.iloc[:, 0], cmap='tab10')
    remaining_axes[2].scatter(sixth_transformed_umap_array[:, 0], sixth_transformed_umap_array[:, 1],
                              c=copy_of_normalized_dataframe.iloc[:, 0], cmap='tab10')
    remaining_axes[0].set_title("n_neighbors=5, min_dist=0.6", color='black', fontsize=16)
    remaining_axes[1].set_title("n_neighbors=25, min_dist=0.6", color='black', fontsize=16)
    remaining_axes[2].set_title("n_neighbors=50, min_dist=0.6", color='black', fontsize=16)

    matplotlib.pyplot.show()

    print("UMAP n_neighbors=5, min_dist=0.1: ", "--- %s seconds --- "
          % (get_current_time() - start_of_first_time_range))
    print("UMAP n_neighbors=25, min_dist=0.1: ", "--- %s seconds --- "
          % (get_current_time() - start_of_second_time_range))
    print("UMAP n_neighbors=50, min_dist=0.1: ", "--- %s seconds --- "
          % (get_current_time() - start_of_third_time_range))
    print("UMAP n_neighbors=5, min_dist=0.6: ", "--- %s seconds --- "
          % (get_current_time() - start_of_fourth_time_range))
    print("UMAP n_neighbors=25, min_dist=0.6: ", "--- %s seconds --- "
          % (get_current_time() - start_of_fifth_time_range))
    print("UMAP n_neighbors=50, min_dist=0.6: ", "--- %s seconds --- "
          % (get_current_time() - start_of_sixth_time_range))


if __name__ == '__main__':
    visualize_dataframe_using_umap(get_dataframe_from(read_data_from('Mall_Customers.csv')))

import pandas
import matplotlib.pyplot
import seaborn
import time
from sklearn import preprocessing
from sklearn.manifold import TSNE


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def get_dataframe_from(data_from_csv_file):
    return pandas.DataFrame(data_from_csv_file)


def get_normalized_dataframe_from(denormalized_dataframe):
    return pandas.DataFrame(preprocessing.MinMaxScaler().fit_transform(denormalized_dataframe),
                            columns=denormalized_dataframe.columns)


def get_current_time():
    return time.time()


def visualize_dataframe_using_tsne(dataframe):
    new_dataframe = dataframe.drop(['CustomerID', 'Gender'], axis=1)
    normalized_dataframe = get_normalized_dataframe_from(new_dataframe)
    first_tsne = TSNE(n_components=2, perplexity=5, random_state=123)
    second_tsne = TSNE(n_components=2, perplexity=25, random_state=123)
    third_tsne = TSNE(n_components=2, perplexity=50, random_state=123)
    first_transformed_array = first_tsne.fit_transform(normalized_dataframe)
    second_transformed_array = second_tsne.fit_transform(normalized_dataframe)
    third_transformed_array = third_tsne.fit_transform(normalized_dataframe)

    copy_of_normalized_dataframe = normalized_dataframe.copy()
    copy_of_normalized_dataframe['x'] = first_transformed_array[:, 0]
    copy_of_normalized_dataframe['y'] = first_transformed_array[:, 1]
    copy_of_normalized_dataframe['x1'] = second_transformed_array[:, 0]
    copy_of_normalized_dataframe['y1'] = second_transformed_array[:, 1]
    copy_of_normalized_dataframe['x2'] = third_transformed_array[:, 0]
    copy_of_normalized_dataframe['y2'] = third_transformed_array[:, 1]

    figure = matplotlib.pyplot.Figure()
    seaborn.scatterplot(x='x', y='y', hue=new_dataframe['Age'],
                        data=copy_of_normalized_dataframe, palette='bright')
    start_of_first_time_range = get_current_time()
    matplotlib.pyplot.show()
    seaborn.scatterplot(x='x1', y='y1', hue=new_dataframe['Age'],
                        data=copy_of_normalized_dataframe, palette='bright')
    start_of_second_time_range = get_current_time()
    matplotlib.pyplot.show()
    seaborn.scatterplot(x='x2', y='y2', hue=new_dataframe['Age'],
                        data=copy_of_normalized_dataframe, palette='bright')
    start_of_third_time_range = get_current_time()
    matplotlib.pyplot.show()

    print("t-SNE, perplexity=5: ", "--- %s seconds --- " % (get_current_time() - start_of_first_time_range))
    print("t-SNE, perplexity=25: ", "--- %s seconds --- " % (get_current_time() - start_of_second_time_range))
    print("t-SNE, perplexity=50: ", "--- %s seconds --- " % (get_current_time() - start_of_third_time_range))


if __name__ == '__main__':
    visualize_dataframe_using_tsne(get_dataframe_from(read_data_from('Mall_Customers.csv')))
    #dataframe = get_dataframe_from(read_data_from('Mall_Customers.csv'))
    #new_dataframe = dataframe.drop(['CustomerID', 'Gender'], axis=1)
    #normalized_dataframe = get_normalized_dataframe_from(new_dataframe)
    #print(normalized_dataframe)

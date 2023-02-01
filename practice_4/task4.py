import pandas
import matplotlib.pyplot
from scipy.stats import iqr as get_interquartile_range_from


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


def add_histogram_with_legend_and_vertical_lines_to_axes_using(data_from_csv_file, axes):
    axes[0].hist(data_from_csv_file['bmi'], edgecolor='black', color='green', bins=15, label='bins = 15')
    axes[0].axvline(data_from_csv_file['bmi'].mean(), color='red', linestyle='dashed', linewidth=2,
                    label='Average value')
    axes[0].axvline(data_from_csv_file['bmi'].median(), color='blue', linestyle='dashed', linewidth=2,
                    label='Median')
    axes[0].legend()
    axes[1].hist(data_from_csv_file['age'], edgecolor='black', color='green', bins=15, label='bins = 15')
    axes[1].legend()
    axes[2].hist(data_from_csv_file['charges'], edgecolor='black', color='green', bins=5, label='bins = 5')
    axes[2].axvline(data_from_csv_file['charges'].std(), color='red', linestyle='dashed', linewidth=2,
                    label='Standard deviation')
    axes[2].axvline(data_from_csv_file['charges'].max() - data_from_csv_file['charges'].min(), color='blue',
                    linestyle='dashed', linewidth=2, label='Range')
    axes[2].axvline(get_interquartile_range_from(data_from_csv_file['charges'], interpolation='midpoint'),
                    color='yellow', linestyle='dashed', linewidth=2, label='Interquartile range')
    axes[2].legend()
    axes[3].hist(data_from_csv_file['children'], edgecolor='black', color='green', bins=5, label='bins = 5')
    axes[3].legend()
    return axes


def add_title_with_labels_to_axes(axes):
    axes[0].set_title('Diagram of bmi', color='black', fontsize=16)
    axes[0].set_xlabel('bmi', color='black', fontsize=16)
    axes[0].set_ylabel('People', color='black', fontsize=16)
    axes[1].set_title('Diagram of age', color='black', fontsize=16)
    axes[1].set_xlabel('age', color='black', fontsize=16)
    axes[1].set_ylabel('People', color='black', fontsize=16)
    axes[2].set_title('Diagram of charges', color='black', fontsize=16)
    axes[2].set_xlabel('charges', color='black', fontsize=16)
    axes[2].set_ylabel('People', color='black', fontsize=16)
    axes[3].set_title('Diagram of children count', color='black', fontsize=16)
    axes[3].set_xlabel('children', color='black', fontsize=16)
    axes[3].set_ylabel('People', color='black', fontsize=16)
    return axes


def display_window_with_histogram_and_measures_of_central_tendency_using(data_from_csv_file):
    pandas.set_option('display.max_columns', None)
    window, axes = matplotlib.pyplot.subplots(1, 4, figsize=(15, 4))
    axes_with_histogram_and_legend = add_histogram_with_legend_and_vertical_lines_to_axes_using(data_from_csv_file,
                                                                                                axes)
    axes_with_title_and_labels = add_title_with_labels_to_axes(axes_with_histogram_and_legend)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    display_window_with_histogram_and_measures_of_central_tendency_using(read_data_from('insurance.csv'))

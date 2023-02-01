from sklearn.datasets import fetch_california_housing
import pandas


def get_california_housing_data_with_average_prices():
    california_housing_data = fetch_california_housing(as_frame=True)
    average_house_prices = california_housing_data.target.to_frame()
    housing_data_with_average_prices = pandas.concat([california_housing_data.data, average_house_prices], axis=1)
    return housing_data_with_average_prices


def load_data_by_criteria_from(dataframe):
    return dataframe.loc[(dataframe["HouseAge"] > 50) & (dataframe["Population"] > 2500)]


if __name__ == '__main__':
    housing_data = get_california_housing_data_with_average_prices()
    print(load_data_by_criteria_from(housing_data))

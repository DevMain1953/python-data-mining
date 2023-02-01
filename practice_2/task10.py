from sklearn.datasets import fetch_california_housing
import pandas


def get_california_housing_data_with_average_prices():
    california_housing_data = fetch_california_housing(as_frame=True)
    average_house_prices = california_housing_data.target.to_frame()
    housing_data_with_average_prices = pandas.concat([california_housing_data.data, average_house_prices], axis=1)
    return housing_data_with_average_prices


if __name__ == '__main__':
    california_housing_data_with_average_prices = get_california_housing_data_with_average_prices()
    print("Minimal average price ", california_housing_data_with_average_prices["MedHouseVal"].min())
    print("Maximal average price ", california_housing_data_with_average_prices["MedHouseVal"].max())

from sklearn.datasets import fetch_california_housing


def get_california_housing_data():
    california_housing_data = fetch_california_housing(as_frame=True)
    return california_housing_data


if __name__ == '__main__':
    print(get_california_housing_data())

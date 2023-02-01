import pandas
from scipy.stats import chi2_contingency as perform_chi_square_test_for_independence_of_variables_in


def create_dataframe():
    dataframe = pandas.DataFrame({'Женат': [89, 17, 11, 43, 22, 1],
                                  'Гражданский брак': [80, 22, 20, 35, 6, 4],
                                  'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]})
    dataframe.index = ['Полный рабочий день', 'Частитчная занятость', 'Временно не работает', 'На домохозяйстве',
                       'На пенсии', 'Учёба']
    return dataframe


if __name__ == '__main__':
    new_dataframe = create_dataframe()
    print(new_dataframe)
    dependecny = perform_chi_square_test_for_independence_of_variables_in(new_dataframe)[:3]
    print("Проверка на зависимость с помощью Хи-квадрат: ", dependecny)

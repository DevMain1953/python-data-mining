from scipy.stats import f_oneway
import statsmodels.api
from statsmodels.formula.api import ols
import pandas


def read_data_from(csv_file):
    return pandas.read_csv(csv_file)


if __name__ == '__main__':
    data_from_csv_file = read_data_from('insurance.csv')
    data_without_duplicates = data_from_csv_file.drop_duplicates()
    dataframe = pandas.DataFrame({'region': data_without_duplicates['region'], 'bmi': data_without_duplicates['bmi']})
    fitted_model = ols('bmi ~ region', data=dataframe).fit()
    anova_table = statsmodels.api.stats.anova_lm(fitted_model, typ=2)
    print(anova_table)

import pandas
import matplotlib.pyplot
import matplotlib.colors
from itertools import accumulate


def read_data_from(url_to_csv):
    return pandas.read_csv(url_to_csv)


def display_window_with_bar_chart_using(dataframe):
    window, axis = matplotlib.pyplot.subplots()

    axis.bar(dataframe.Date[::365], dataframe.Close[::365],
             color='#00FF00',
             edgecolor='#000000',
             linewidth=2)
    window.set_figwidth(12)
    window.set_figheight(6)
    axis.set_facecolor('#BEBEBE')
    matplotlib.pyplot.subplots_adjust(bottom=0.20)
    matplotlib.pyplot.xticks(rotation=45)
    axis.set_xlabel('Дата')
    axis.set_ylabel('Цена закрытия в $')
    matplotlib.pyplot.title('Акции GE')
    matplotlib.pyplot.show()


def display_window_with_pie_chart_using(dataframe):
    window, axis = matplotlib.pyplot.subplots()

    axis.pie(dataframe.Close[:10:], labels=dataframe.Date[:10:])
    window.set_figwidth(12)
    window.set_figheight(6)
    axis.set_facecolor('#BEBEBE')
    matplotlib.pyplot.subplots_adjust(bottom=0.20)
    matplotlib.pyplot.xticks(rotation=45)
    axis.set_xlabel('Дата')
    axis.set_ylabel('Цена закрытия в $')
    matplotlib.pyplot.title('Акции GE')
    matplotlib.pyplot.show()


def display_window_with_line_graph_using(dataframe):
    window, axis = matplotlib.pyplot.subplots()

    axis.scatter(dataframe.Date[::365],
                 list(accumulate(dataframe.Close[::365], lambda x, y: x + y)),
                 color="darkblue",
                 edgecolor='#000000',
                 linewidth=2)

    axis.plot(dataframe.Date[::365],
              list(accumulate(dataframe.Close[::365], lambda x, y: x + y)),
              color='crimson',
              linewidth=2)
    window.set_figwidth(12)
    window.set_figheight(6)
    axis.set_facecolor('#BEBEBE')
    matplotlib.pyplot.subplots_adjust(bottom=0.20)
    matplotlib.pyplot.xticks(rotation=45)
    axis.set_xlabel('Дата')
    axis.set_ylabel('Цена закрытия в $')
    matplotlib.pyplot.title('Акции GE')
    matplotlib.pyplot.show()


if __name__ == '__main__':
    csv_data = read_data_from("https://query1.finance.yahoo.com/v7/finance/download/GE?period1=-252374400&period2="
                              "1663718400&interval=1d&events=history&includeAdjustedClose=true")

    date_and_close = pandas.concat([csv_data.Date, csv_data.Close], axis=1)
    display_window_with_line_graph_using(date_and_close)

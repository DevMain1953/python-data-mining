import pandas
import plotly


def read_data_from(url_to_csv):
    return pandas.read_csv(url_to_csv)


def create_pie_chart_from(dataframe):
    content_of_chart = plotly.graph_objs.Pie(labels=dataframe.Date[::365],
                                             values=dataframe.Close[::365],
                                             marker_line=dict(width=2, color='#000000'))

    layout_of_chart = plotly.graph_objs.Layout(paper_bgcolor='#FFFFFF',
                                               plot_bgcolor='#BEBEBE',
                                               title={'font': dict(size=20),
                                                      'x': 0.5,
                                                      'text': 'Акции GE'},
                                               xaxis=dict(title='Дата',
                                                          title_font_size=16,
                                                          tickfont_size=14,
                                                          tickangle=315),
                                               yaxis=dict(title='Цена закрытия в $',
                                                          title_font_size=16,
                                                          tickfont_size=14),
                                               height=700,
                                               width=None,
                                               margin=dict(l=40, r=40, t=40, b=40))

    pie_chart = plotly.graph_objs.Figure(data=content_of_chart, layout=layout_of_chart)
    return pie_chart


if __name__ == '__main__':
    csv_data = read_data_from("https://query1.finance.yahoo.com/v7/finance/download/GE?period1=-252374400&period2="
                              "1663718400&interval=1d&events=history&includeAdjustedClose=true")

    date_and_close = pandas.concat([csv_data.Date, csv_data.Close], axis=1)
    create_pie_chart_from(date_and_close).show()

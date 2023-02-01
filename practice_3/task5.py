import pandas
import plotly
from itertools import accumulate


def read_data_from(url_to_csv):
    return pandas.read_csv(url_to_csv)


def create_line_graph_from(dataframe):
    dots_on_graph = plotly.graph_objs.Scatter(x=dataframe.Date[::365],
                                              y=list(accumulate(dataframe.Close[::365], lambda x, y: x + y)),
                                              # we just need string to describe color
                                              marker_color="darkblue",
                                              marker_line=dict(width=2, color='black'),
                                              mode="markers")

    line_on_graph = plotly.graph_objs.Scatter(x=dataframe.Date[::365],
                                              y=list(accumulate(dataframe.Close[::365], lambda x, y: x + y)),
                                              # we just need string to describe color
                                              marker_color="crimson",
                                              marker_line=dict(width=2, color='black'),
                                              mode="lines")

    layout_of_graph = plotly.graph_objs.Layout(paper_bgcolor='#FFFFFF',
                                               plot_bgcolor="azure",
                                               title={'font': dict(size=20),
                                                      'x': 0.5,
                                                      'text': 'Акции GE'},
                                               xaxis=dict(title='Дата', title_font_size=16, tickfont_size=14,
                                                          tickangle=315),
                                               yaxis=dict(title='Цена закрытия в $', title_font_size=16,
                                                          tickfont_size=14),
                                               height=700,
                                               width=None,
                                               margin=dict(l=40, r=40, t=40, b=40),
                                               legend=dict(yanchor="bottom", y=-0.2, xanchor="left", x=0.01))

    line_graph = plotly.graph_objs.Figure(data=line_on_graph, layout=layout_of_graph)
    line_graph.add_trace(dots_on_graph)
    line_graph.update_xaxes(showline=True, linewidth=2, gridcolor='ivory')
    line_graph.update_yaxes(showline=True, linewidth=2, gridcolor='ivory')
    return line_graph


if __name__ == '__main__':
    csv_data = read_data_from("https://query1.finance.yahoo.com/v7/finance/download/GE?period1=-252374400&period2="
                              "1663718400&interval=1d&events=history&includeAdjustedClose=true")

    date_and_close = pandas.concat([csv_data.Date, csv_data.Close], axis=1)
    create_line_graph_from(date_and_close).show()

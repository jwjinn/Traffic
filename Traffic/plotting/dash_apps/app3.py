from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *
# ImportError: attempted relative import with no known parent package
app = DjangoDash('BarPopulation')

SeoulIndex = Seoulindex.objects.all().values()
Coordinate = Coordinate.objects.all().values()


Coordinate = pd.DataFrame(Coordinate)
SeoulIndex = pd.DataFrame(SeoulIndex)

SeoulIndex = SeoulIndex.iloc[:, 0:3]

# print(SeoulIndex)
# print(Coordinate)

# print(pd.merge(SeoulIndex, Coordinate, left_on='gu', right_on='gu_id'))
df = pd.merge(SeoulIndex, Coordinate, left_on='gu', right_on='gu_id')



app.layout = html.Div(
children=[

    dcc.RadioItems([{"label": "12세이상 인구수", "value": 'population_over12'}, 
                    {"label": "통근 인구수", "value": 'commute_population'}], 
                    'population_over12',
                    id = 'yaxis-type',
                    inline= True),

    dcc.Graph(id = 'indicator-graphic-line'),
    dcc.Graph(id = 'indicator-graphic-pie')
])

@app.callback(
    Output('indicator-graphic-line', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):

    # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    fig = px.bar(df, x="gu",
                y=yaxis_type,
                barmode="group",
                )
    fig.update_layout(xaxis_title="", yaxis_title="(명)")
    fig.update_yaxes(tickformat=",")
    fig.update_traces(hovertemplate="%{x}"+"<br>%{y}명")
    # fig = px.pie(df, values = yaxis_type, names='gu')
    #
    # fig = px.line(df, x = 'gu', y = yaxis_type)

    return fig

@app.callback(
    Output('indicator-graphic-pie', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):

    # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    # fig = px.bar(df, x="gu",
    #              y=yaxis_type,
    #              color="gu", barmode="group")

    fig = px.pie(df, values = yaxis_type, names='gu',
                custom_data=["gu", yaxis_type])
    fig.update_traces(hovertemplate="%{customdata[0]}명")


    return fig
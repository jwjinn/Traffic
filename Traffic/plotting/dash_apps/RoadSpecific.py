from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *
# ImportError: attempted relative import with no known parent package
app = DjangoDash('AdjustRoad')

Road = Adjustroad.objects.all().values()
Road = pd.DataFrame(Road)
Road['day'] = pd.to_datetime(Road['day'], format = "%Y-%m-%d")


Road = Road.set_index('day')

app.layout = html.Div(
children=[

    html.Div([
        dcc.Dropdown(
            Road['name'].unique(),
            '강남대로(강남역-신분당)',
            id='SelectLocation'
        )

    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown([
                    {"label": "월 평균", "value": 'mean_month'}, 
                    {"label": "전체", "value": 'vol_month'}], 
                    'mean_month',
                    id = 'yaxis',

        ),

    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic'),

    dcc.RadioItems(['2018', '2019', '2020', '2021', '2022'], '2018'
                   , id='year',
                   inline=True),
])
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('SelectLocation', 'value'),
    Input('yaxis', 'value'),
    Input('year', 'value')
)
def update_graph(selectlocation, yaxis, year):

    df = Road.loc[year][Road.loc[year]['name'] == selectlocation]

    fig = px.line(df, x = df.index.values, y = yaxis)
    fig.update_layout(xaxis_title="", yaxis_title="(대)")
    fig.update_yaxes(tickformat=",")
    fig.update_traces(hovertemplate="%{x}"+"<br>%{y}대")
    return fig



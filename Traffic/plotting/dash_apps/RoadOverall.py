from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *
# ImportError: attempted relative import with no known parent package
app = DjangoDash('RoadOverall')

Road = Adjustroad.objects.all().values()
Road = pd.DataFrame(Road)
Road['day'] = pd.to_datetime(Road['day'], format = "%Y-%m-%d")


print(Road)
print("---------------")
print(Road.info())

app.layout = html.Div(
children=[

    html.Div([
        dcc.Dropdown(
            Road['name'].unique(),
            '강남대로(강남역-신분당)',
            id='SelectLocation'
        )

    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic'),

    ])
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('SelectLocation', 'value'),
)
def update_graph(selectlocation):


    fig = px.line(Road[Road['name'] == selectlocation], x = 'day', y = 'mean_month')

    return fig






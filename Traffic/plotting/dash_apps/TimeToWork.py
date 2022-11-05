from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *


# ImportError: attempted relative import with no known parent package
app = DjangoDash('TimeToWork')

Time = Timetowork.objects.all().values()
Time = pd.DataFrame(Time)

df = Time

app.layout = html.Div(

    children=[

    dcc.RadioItems([{"label": "전체", "value": 'total'}, 
                    {"label": "남자", "value": 'men'}, 
                    {"label": "여자", "value": 'women'}], 
                    'total',
                    id='yaxis-type',
                    inline=True),

        dcc.Graph(
        id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):

    fig = px.bar(df, x="country",
                y=yaxis_type,
                barmode="group")
    fig.update_layout(xaxis_title="", yaxis_title="(시간)")
    fig.update_traces(hovertemplate="국가: %{x}"+"<br>출퇴근시간: %{y}시간")
    return fig

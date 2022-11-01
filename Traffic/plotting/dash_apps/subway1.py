import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import datetime

app = DjangoDash("day")

data = Subway.objects.all().values()
df = pd.DataFrame(data)

app.layout = html.Div([
    dcc.Dropdown(
        id="date",
        options=[{"label": x, "value": x} for x in df["day"].unique()],
        value=datetime.date(2022,9,1),
        clearable=False,
        ),

    dcc.RadioItems(
        id="click",
        options=[{"label": "boarding", "value": "boarding"},
                {"label": "getoff", "value": "getoff"}],
        value="boarding",
        inline=True,
    ),

    dcc.Graph(id="graph", figure={}),
])


@app.callback(Output("graph", "figure"), [Input("date", "value"), Input("click", "value")])
def cb(date, item):
    y = int(date[:4])
    m = int(date[5:7])
    d = int(date[8:10])
    df_date = df[df["day"] == datetime.date(y,m,d)]
    # print(date)
    if item == "boarding":
        fig = px.scatter(df_date, x="gu_id", y="boarding", color="gu_id")
    elif item == "getoff":
        fig = px.scatter(df_date, x="gu_id", y="getoff", color="gu_id")
    fig.update_yaxes(range=[0, 18000000])
    fig.update_xaxes(visible=False)
    return fig

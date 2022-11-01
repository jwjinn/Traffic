import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import datetime

app = DjangoDash("gu")

data = Subway.objects.all().values()
df = pd.DataFrame(data)

app.layout = html.Div([
    dcc.Dropdown(
        id="gu",
        options=[{"label": x, "value": x} for x in df["gu_id"].unique()],
        value="강남구",
        clearable=False,
        ),
    dcc.Graph(id="graph", figure={}),
])


@app.callback(Output("graph", "figure"), [Input("gu", "value")])
def cb(gu):
    print(gu)
    df_gu = df[df["gu_id"] == gu]
    fig = px.line(df_gu, x="day", y="boarding")
    fig.update_yaxes(range=[0, 18000000])
    # fig.update_xaxes(visible=False)
    return fig


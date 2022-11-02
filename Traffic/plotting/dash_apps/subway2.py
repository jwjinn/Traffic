import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import datetime

app = DjangoDash("subway2")

data = Subway.objects.all().values()
df = pd.DataFrame(data)

app.layout = html.Div([
    dcc.Dropdown(
        id="gu",
        options=[{"label": x, "value": x} for x in df["gu_id"].unique()],
        value="강남구",
        clearable=False,
        ),
    dcc.RadioItems(
        id="click",
        options=[{"label": "승차", "value": "boarding"},
                {"label": "하차", "value": "getoff"}],
        value="boarding",
        inline=True,
    ),
    dcc.Graph(id="graph", figure={}),
])


@app.callback(Output("graph", "figure"), [Input("gu", "value"), Input("click", "value")])
def cb(gu, item):
    print(gu)
    df_gu = df[df["gu_id"] == gu]
    if item == "boarding":
        fig = px.line(df_gu, x="day", y="boarding")
        fig.update_layout(xaxis_title="", yaxis_title="승차")
    elif item == "getoff":
        fig = px.line(df_gu, x="day", y="getoff")
        fig.update_layout(xaxis_title="", yaxis_title="승차")
    fig.update_xaxes(visible=False)
    
    # fig.update_xaxes(visible=False)
    return fig


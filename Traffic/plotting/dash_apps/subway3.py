import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import datetime


app = DjangoDash("subway3")

data = Subway.objects.all().values()
df = pd.DataFrame(data)
df = df.groupby(by=["day"]).sum().reset_index()
df["day"] = df["day"].apply(str)
years = ['2019', '2020', '2021', '2022']
df["year"] = df["day"].str[:4]

app.layout = html.Div([
    dcc.Dropdown(
        id="multi",
        options=[{"label": y, "value": y} for y in years],
        value="2022",
        multi=True,
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


@app.callback(Output("graph", "figure"), [Input("multi", "value"), Input("click", "value")])
def cb(year, item):
    print(year)
    if type(year) == str:
        year = [year]
    print(year)
    df_year = df[df["day"].str[:4].isin(year)]
    if item == "boarding":
        fig = px.scatter(df_year, x="day", y="boarding", color="year", size="boarding", labels={"year": ""})
        fig.update_layout(xaxis_title="", yaxis_title="승차")
    elif item == "getoff":
        fig = px.scatter(df_year, x="day", y="getoff", color="year", size="boarding", labels={"year": ""})
        fig.update_layout(xaxis_title="", yaxis_title="하차")
    return fig


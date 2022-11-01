import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import datetime


app = DjangoDash("multi")

data = Subway.objects.all().values()
df = pd.DataFrame(data)
df = df.groupby(by=["day"]).sum().reset_index()
df["day"] = df["day"].apply(str)
years = ['2019', '2020', '2021', '2022']


app.layout = html.Div([
    dcc.Dropdown(
        id="multi",
        options=[{"label": y, "value": y} for y in years],
        value="2022",
        multi=True,
        clearable=False,
        ),
    dcc.Graph(id="graph", figure={})
])


@app.callback(Output("graph", "figure"), [Input("multi", "value")])
def cb(year):
    print(year)
    if type(year) == str:
        year = [year]
    print(year)
    df_year = df[df["day"].str[:4].isin(year)]

    fig = px.scatter(df_year, x="day", y="boarding", color="day", size="boarding")
    range_list = [x for x in df_year["day"].unique()]
    print(range_list)
    # fig.update_xaxes(tickvals = range_list)
    return fig


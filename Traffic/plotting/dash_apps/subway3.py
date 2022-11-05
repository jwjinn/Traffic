import pandas as pd
import plotly.express as px

from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway


app = DjangoDash("subway3")

data = Subway.objects.all().values()
df = pd.DataFrame(data)
df = df.groupby(by=["day"]).sum().reset_index()
years = ['2019', '2020', '2021', '2022']
df["day"] = df["day"].apply(str)
df["day"] = df["day"].str[:7]
df["year"] = df["day"].str[:4]
df["boarding"] = df["boarding"] // 10000
df["getoff"] = df["getoff"] // 10000

app.layout = html.Div([
    dcc.Dropdown(
        id="multi",
        options=[{"label": y, "value": y} for y in years],
        value="2022",
        multi=True,
        clearable=False,
        ),
    html.Br(),
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
    # print(df_year["day"].iloc[0])
    if item == "boarding":
        fig = px.scatter(df_year, x="day", y="boarding", color="year", size="boarding", symbol="year", labels={"year": ""})
        fig.update_layout(xaxis_title="", yaxis_title="(만명)", hovermode="x")
    elif item == "getoff":
        fig = px.scatter(df_year, x="day", y="getoff", color="year", size="getoff", symbol="year", labels={"year": ""})
        fig.update_layout(xaxis_title="", yaxis_title="(만명)", hovermode="x")
    
    fig.update_yaxes(tickformat=",")
    fig.update_traces(hovertemplate="%{x}"+"<br>%{y}만명")
    return fig


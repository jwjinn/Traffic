import pandas as pd
import plotly.express as px

from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway


app = DjangoDash("subway2")

data = Subway.objects.all().values()
df = pd.DataFrame(data)
df["boarding"] = df["boarding"] // 10000
df["getoff"] = df["getoff"] // 10000

app.layout = html.Div([
    dcc.Dropdown(
        id="gu",
        options=[{"label": x, "value": x} for x in df["gu_id"].unique()],
        value="강남구",
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


@app.callback(Output("graph", "figure"), [Input("gu", "value"), Input("click", "value")])
def cb(gu, item):
    print(gu)
    df_gu = df[df["gu_id"] == gu]
    if item == "boarding":
        fig = px.line(df_gu, x="day", y="boarding", line_shape='spline')
        fig.update_layout(xaxis_title="", yaxis_title="(만명)", hovermode="x")
    elif item == "getoff":
        fig = px.line(df_gu, x="day", y="getoff", line_shape='spline')
        fig.update_layout(xaxis_title="", yaxis_title="(만명)", hovermode="x")
    fig.update_xaxes(visible=False)
    fig.update_yaxes(tickformat=",")
    fig.update_traces(hovertemplate="%{x}"+"<br>%{y}만명")
    
    
    return fig


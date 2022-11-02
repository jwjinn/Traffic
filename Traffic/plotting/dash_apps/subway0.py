import pandas as pd
from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Subway, Avgsubway

import plotly.express as px


app = DjangoDash("subway0")

data = Subway.objects.all().values()
data_avg = Avgsubway.objects.all().values()
df = pd.DataFrame(data)
df_avg = pd.DataFrame(data_avg)
df_total = df.groupby(by=["day"]).sum().reset_index()
df_total["total"] = df_total["boarding"] + df_total["getoff"]
df_total_avg = df_avg.groupby(by=["day"]).sum().reset_index()
df_total_avg["total"] = df_total_avg["boarding"] + df_total_avg["getoff"]


app.layout = html.Div([
    dcc.RadioItems(
        id="click",
        options=[{"label": "전체", "value": "Total"},
                {"label": "평균", "value": "Average"}], 
        value="Total", 
        inline=True),

    dcc.Graph(id="graph", figure={}),
])

@app.callback(Output("graph", "figure"), [Input("click", "value")])
def cb(item):
    # print(item)
    if item == "Total":
        fig = px.scatter(df_total, x="day", y="total", color="day")
        
    elif item == "Average":
        fig = px.scatter(df_total_avg, x="day", y="total", color="day")
    fig.update_layout(
                    xaxis_title="", 
                    yaxis_title="", 
                    showlegend=False)
    
    return fig


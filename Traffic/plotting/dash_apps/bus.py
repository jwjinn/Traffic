import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
from django_plotly_dash import DjangoDash
from ..models import Bus
import plotly.express as px
import datetime

data = Bus.objects.all().values()

df= pd.DataFrame(data)
df['total'] = df.sum(axis=1)
df['total'] = df['total'] // 10000
df["boarding"] = df["boarding"] // 10000
df["getoff"] = df["getoff"] // 10000


app = DjangoDash("total")
fig = figure=px.line(df, x='day', y='total', color='gu_id', line_shape='spline', render_mode='svg', labels={"gu_id": ""},
                    custom_data=["gu_id"])
fig.update_layout(xaxis_title="", yaxis_title="(만명)", yaxis= dict(tickformat = ","))
fig.update_traces(hovertemplate="%{customdata[0]}"+"<br>%{x}"+"<br>%{y}명")

app.layout = html.Div([
    dcc.Graph(id='graph01', figure=fig, style={'width':'100%'}
)])

##

app2 = DjangoDash("byMonth")
app2.layout = html.Div([
    dcc.Dropdown(
        id="date",
        options=[{"label": f"{x.year}년 {x.month}월", "value": x} for x in df["day"].unique()],
        value=datetime.date(2022,9,1),
        clearable=False,
        ),
    dcc.Graph(id='graph02', figure={}),
])
@app2.callback(Output('graph02','figure'), [Input('date','value')])
def cb(date):
    y = int(date[:4])
    m = int(date[5:7])
    d = int(date[8:10])
    df_date = df[df["day"] == datetime.date(y,m,d)]
    print(df_date)
    fig = px.scatter(df_date, x='gu_id', y='total' ,color='gu_id',size='total', labels={"gu_id": ""}).update_layout(
    xaxis_title="자치구", yaxis_title="승하차량"
)
    fig.update_yaxes(range=[0, 2000], tickformat=",")
    fig.update_layout(xaxis_title="", yaxis_title="(만명)")
    fig.update_traces(hovertemplate="%{x}"+"<br>%{y}명")
    return fig

app3 = DjangoDash("Animation")
fig =  px.scatter(df, x="boarding", y="getoff", animation_frame="day", animation_group="gu_id",size="total", color="gu_id", hover_name="gu_id",log_x=True, size_max=55, range_x=[100, 2000], range_y=[0, 2000], labels={"gu_id": ""},
                custom_data=["gu_id", "total"])
fig.update_layout(xaxis_title="승차량(만명)", yaxis_title="하차량(만명)")
fig.update_traces(hovertemplate="%{customdata[0]}"+
                    "<br>승차인원: %{x}만명"+
                    "<br>하차인원: %{y}만명"+
                    "<br>총: %{customdata[1]}만명")
app3.layout = html.Div([
    dcc.Graph(id='graph03', figure = fig)
    ])
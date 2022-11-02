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


app = DjangoDash("total")
app.layout = html.Div([
    
    html.H1(
        children='승하차량',
        style={
            'textAlign':'center',
            'color':'black'
        }
    ),
    dcc.Graph(id='graph01', figure=px.line(df, x='day', y='total' ,color='gu_id',hover_name='gu_id',line_shape='spline',render_mode='svg').update_layout(
    xaxis_title="", yaxis_title="승하차량"
),style={'width':'100%'}
)])

##

app2 = DjangoDash("byMonth")
app2.layout = html.Div([
        html.H1(
        children='월별 승차인원',
        style={
            'textAlign':'center',
            'color':'black'
        }
    ),
     dcc.Dropdown(
        id="date",
        options=[{"label": x, "value": x} for x in df["day"].unique()],
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
    fig = px.scatter(df_date, x='gu_id', y='total' ,color='gu_id',size='getoff').update_layout(
    xaxis_title="자치구", yaxis_title="승하차량"
)
    fig.update_yaxes(range=[0, 18000000])
    return fig

app3 = DjangoDash("Animation")
app3.layout = html.Div([
    html.H1(
        children='승하차량',
        style={
            'textAlign':'center',
            'color':'black'
        }
    ),
    dcc.Graph(id='graph03', figure = px.scatter(df, x="boarding", y="getoff", animation_frame="day", animation_group="gu_id",size="total", color="gu_id", hover_name="gu_id",log_x=True, size_max=55, range_x=[2000000,15000000], range_y=[1500000,15000000]).update_layout(
    xaxis_title="승차량", yaxis_title="하차량"
))
    ])
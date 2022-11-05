from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *
# ImportError: attempted relative import with no known parent package
app = DjangoDash('RoadByYear')

Road = Adjustroad.objects.all().values()
Road = pd.DataFrame(Road)
Road['day'] = pd.to_datetime(Road['day'], format = "%Y-%m-%d")
Road['year'] = Road['day'].dt.year

by_year = Road[['year', 'vol_month']]

temp = by_year.groupby('year').mean('vol_month')
temp = temp.astype({"vol_month": int})

fig = px.line(temp, x = temp.index.values, y = 'vol_month', markers=True)
fig.update_layout(xaxis_title="", yaxis_title="(대)")
fig.update_yaxes(tickformat=",")
fig.update_traces(hovertemplate="%{x}년도"+"<br>연평균 통행량: %{y}대")
app.layout = html.Div(
    dcc.Graph(
        id='example-graph',
        figure=fig,
        # style={'width': '90px', 'height' : '500px'}
    )

)











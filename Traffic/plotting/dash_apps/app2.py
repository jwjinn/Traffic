from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash

from ..models import *

app = DjangoDash('SimpleExample2')


SeoulIndex = Seoulindex.objects.all().values()
Coordinate = Coordinate.objects.all().values()


Coordinate = pd.DataFrame(Coordinate)
SeoulIndex = pd.DataFrame(SeoulIndex)

SeoulIndex = SeoulIndex.iloc[:, 0:3]

# print(SeoulIndex)
# print(Coordinate)
#
# print(pd.merge(SeoulIndex, Coordinate, left_on='gu', right_on='gu_id'))
df = pd.merge(SeoulIndex, Coordinate, left_on='gu', right_on='gu_id')

#pk.eyJ1Ijoid29vam9vMTIxIiwiYSI6ImNsOXc2bW1jdzBkNWwzb202dnV1M2I2NHMifQ.U2WIYcpIYLsVjg6gqXMQSQ

px.set_mapbox_access_token('pk.eyJ1Ijoid29vam9vMTIxIiwiYSI6ImNsOXc2bW1jdzBkNWwzb202dnV1M2I2NHMifQ.U2WIYcpIYLsVjg6gqXMQSQ')

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="gu", labels={"gu": ""},
                    size="commute_population", color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)


app.layout = html.Div(

    # style={"background-color":"red", "overflow": "auto"},



    children=[

    dcc.Graph(
        id='example-graph',
        figure=fig,
        # style={'width': '90px', 'height' : '500px'}
    ),




])




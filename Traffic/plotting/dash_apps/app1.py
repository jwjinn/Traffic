from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *


# ImportError: attempted relative import with no known parent package
app = DjangoDash('SimpleExample')


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(

    # style={"background-color":"red", "overflow": "auto"},


    children=[

    dcc.Graph(
        id='example-graph',
        figure=fig,
        # style={'width': '90px', 'height' : '500px'}
    )
])


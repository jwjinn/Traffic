from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *


# ImportError: attempted relative import with no known parent package
app = DjangoDash('TimeToWork')

Time = Timetowork.objects.all().values()
Time = pd.DataFrame(Time)

df = Time

# print(df)
# print(df.info())

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="country", y="total", barmode="group")

app.layout = html.Div(

    children=[

    dcc.RadioItems(['total', 'men', 'women'], 'total'
                    , id='yaxis-type',
                    inline=True),

        dcc.Graph(
        id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('yaxis-type', 'value'),
)
def update_graph(yaxis_type):

    fig = px.bar(df, x="country",
                 y=yaxis_type,
                barmode="group")


    return fig

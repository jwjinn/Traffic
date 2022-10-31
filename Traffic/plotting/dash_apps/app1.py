from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from ..models import Bus

app = DjangoDash('SimpleExample')

datas = Bus.objects.all().values()
# print(datas)
dff = pd.DataFrame(datas)
# print(dff)

# print(int(dff.iloc[1,2]) + int(dff.iloc[1,3]))

print(dff)




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
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        # style={'width': '90px', 'height' : '500px'}
    )
])


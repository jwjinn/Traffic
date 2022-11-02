from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash


# from Traffic.plotting.models import Bus
from ..models import *

app = DjangoDash('AdjustRoadTable')

Road = Adjustroad.objects.all().values()
Road = pd.DataFrame(Road)

app.layout = dash_table.DataTable(
    Road.to_dict('records'), [{"name": i, "id": i} for i in Road.columns])


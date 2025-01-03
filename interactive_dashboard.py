
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import requests

def create_dashboard(server):
    # Create Dash app
    dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

    # Fetch data from the API endpoint
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
    except requests.RequestException as e:
        df = pd.DataFrame({'Error': ['Could not fetch data']})

    # Define layout
    dash_app.layout = html.Div([
        html.H1('Interactive Dashboard with Dynamic Data'),
        dcc.Graph(
            id='example-graph',
            figure=px.bar(df, x='id', y='userId', title='Sample Bar Chart')
        ),
        html.Div("Displaying dynamic data fetched from the API.")
    ])

    return dash_app

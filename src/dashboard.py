# File: src/dashboard.py

import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data for visualization
def load_dashboard_data(file_path: str):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "HyCAN Dashboard"

# Load example dataset
data = load_dashboard_data("data/example_data.csv")

# Layout for the dashboard
app.layout = html.Div([
    html.H1("HyCAN Data Visualization", style={"textAlign": "center"}),

    dcc.Dropdown(
        id="column-dropdown",
        options=[{"label": col, "value": col} for col in data.columns],
        placeholder="Select a column to visualize",
    ),

    dcc.Graph(id="column-graph"),

    html.Div([
        html.H3("Dataset Preview"),
        html.Pre(id="data-preview"),
    ])
])

# Callbacks for interactivity
@app.callback(
    [Output("column-graph", "figure"), Output("data-preview", "children")],
    [Input("column-dropdown", "value")]
)
def update_graph(column_name):
    if not column_name:
        return {}, "Select a column to preview the data."
    
    fig = px.histogram(data, x=column_name, title=f"Distribution of {column_name}")
    preview = data[[column_name]].head().to_string()
    return fig, f"Preview:\n{preview}"

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

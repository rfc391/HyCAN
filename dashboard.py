
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import logging

logging.basicConfig(level=logging.INFO)

def load_dashboard_data(file_path: str):
    try:
        logging.info(f"Loading data from {file_path}")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

app = dash.Dash(__name__)
app.title = "HyCAN Dashboard"

data = load_dashboard_data("data/example_data.csv")
if data is None:
    data = pd.DataFrame(columns=["Column1", "Column2"])

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

if __name__ == "__main__":
    app.run_server(debug=True)

def show_data_summary(data):
    """Computes and returns a summary of the data."""
    import pandas as pd
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    return data.describe()

import plotly.express as px

def create_interactive_plot(data, x_column, y_column):
    """Creates an interactive Plotly figure."""
    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError("Specified columns must exist in the data.")
    fig = px.scatter(data, x=x_column, y=y_column, title=f"Interactive {y_column} vs {x_column}")
    return fig

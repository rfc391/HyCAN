import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "HyCAN Dashboard"

# Global variable to hold data
data = None

# Layout for the dashboard
app.layout = html.Div([
    html.H1("HyCAN Data Visualization", style={"textAlign": "center"}),

    dcc.Dropdown(
        id="column-dropdown",
        options=[],  # To be updated dynamically
        placeholder="Select a column to visualize",
    ),

    dcc.Graph(id="column-graph"),

    html.Div([
        html.H3("Dataset Preview"),
        html.Pre(id="data-preview"),
    ])
])

# Callback to update dropdown options and graph
def update_data(new_data):
    global data
    data = new_data
    app.layout.children[1].options = [
        {"label": col, "value": col} for col in data.columns
    ]

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
    # Example usage with preprocessed data
    mock_data = {
        "column_name": [10, 20, 30, 40, 50],
        "normalized_column": [0.2, 0.4, 0.6, 0.8, 1.0],
        "other_column": ["A", "B", "C", "D", "E"]
    }
    df = pd.DataFrame(mock_data)
    update_data(df)  # Load the example data into the dashboard
    app.run_server(debug=True)

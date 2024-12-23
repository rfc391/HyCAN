
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    app = dash.Dash(__name__)

    # Example data
    data = pd.DataFrame({
        "X": range(10),
        "Y": [x ** 2 for x in range(10)],
        "Category": ["A", "B"] * 5
    })

    app.layout = html.Div([
        html.H1("Interactive Dashboard with Filters"),
        html.Label("Select Category:"),
        dcc.Dropdown(
            id="category-filter",
            options=[{"label": cat, "value": cat} for cat in data["Category"].unique()],
            value="A"
        ),
        dcc.Graph(id="scatter-plot")
    ])

    @app.callback(
        Output("scatter-plot", "figure"),
        [Input("category-filter", "value")]
    )
    def update_plot(selected_category):
        if selected_category not in data["Category"].unique():
            logger.error("Invalid category selected: %s", selected_category)
            return px.scatter(title="Invalid Category")

        logger.info("Updating plot for category: %s", selected_category)
        filtered_data = data[data["Category"] == selected_category]
        fig = px.scatter(filtered_data, x="X", y="Y", title=f"Category: {selected_category}")
        return fig

    if __name__ == "__main__":
        logger.info("Starting Dash server...")
        app.run_server(debug=True)

except Exception as e:
    logger.exception("Failed to start the interactive dashboard: %s", e)


"""
Interactive Visualization for Catalyst Performance
"""
import plotly.express as px
import pandas as pd

class Visualization:
    @staticmethod
    def plot_catalyst_performance(data):
        """
        Creates an interactive plot of catalyst performance.
        :param data: DataFrame
        :return: Plotly Figure
        """
        fig = px.scatter(data, x="catalyst_efficiency", y="yield_rate",
                         color="nanomaterial_type",
                         title="Catalyst Performance Overview")
        fig.show()

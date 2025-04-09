import plotly.express as px
import pandas as pd

def create_scatter_plot(data):
    df = pd.DataFrame(data)
    fig = px.scatter(df, x='time', y='value', color='category')
    fig.show()

import pandas as pd
import matplotlib.pyplot as plt
from src.dashboard import show_data_summary, plot_data

def test_data_summary():
    """Test the data summary function."""
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    summary = data.describe()
    assert summary is not None
    assert "mean" in summary.index

def test_plot_data():
    """Test the plot function."""
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    figure = plt.Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    data.plot(kind='bar', ax=ax)
    assert ax.has_data()


import pandas as pd
from HyCAN-main.show_data_summary import show_data_summary
from HyCAN-main.visualizations.plotter import plot_data

def test_data_summary():
    """Test the data summary function."""
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    summary = show_data_summary(data)
    assert summary is not None
    assert "mean" in summary.index
    assert "A" in summary.columns

def test_plot_data():
    """Test the plot function."""
    data = pd.DataFrame({"X": [1, 2, 3], "Y": [4, 5, 6]})
    try:
        plot_data(data, x_column="X", y_column="Y")
    except Exception as e:
        assert False, f"Plot function raised an exception: {e}"

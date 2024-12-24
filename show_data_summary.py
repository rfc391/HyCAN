
import pandas as pd

def show_data_summary(data):
    """Computes and returns a summary of the data."""
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    return data.describe()

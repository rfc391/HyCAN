
import pandas as pd
from sklearn.preprocessing import StandardScaler

def handle_missing_data(data, strategy="mean"):
    """Fills missing values in a DataFrame using the specified strategy."""
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    if strategy == "mean":
        return data.fillna(data.mean())
    elif strategy == "median":
        return data.fillna(data.median())
    elif strategy == "mode":
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', or 'mode'.")

def scale_data(data, columns):
    """Scales specified columns in a DataFrame using StandardScaler."""
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    scaler = StandardScaler()
    data[columns] = scaler.fit_transform(data[columns])
    return data

def validate_data(data, expected_columns):
    """Validates that a DataFrame contains the expected columns."""
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    missing_columns = set(expected_columns) - set(data.columns)
    if missing_columns:
        raise ValueError(f"Data is missing columns: {missing_columns}")
    return True

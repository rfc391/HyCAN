
def handle_missing_data(data, strategy="mean"):
    """Fills missing values in a DataFrame using the specified strategy."""
    import pandas as pd
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    if data.isnull().values.any():
        print(f"INFO: Handling missing data using strategy '{strategy}'")
    if strategy == "mean":
        return data.fillna(data.mean())
    elif strategy == "median":
        return data.fillna(data.median())
    elif strategy == "mode":
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid strategy. Choose from 'mean', 'median', or 'mode'.")

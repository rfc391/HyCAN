# HyCAN Utilities
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def summarize_data(data):
    print(data.describe())

if __name__ == "__main__":
    print("Run as utility module only.")
"""

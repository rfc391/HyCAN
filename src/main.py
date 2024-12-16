# HyCAN: Main Application
# Author: Robert Shubert
# Description: Entry point for the Hydrogen Catalyst and Nanomaterials project.

import argparse
import pandas as pd

def main(data_path):
    print(f"Analyzing data from: {data_path}")
    data = pd.read_csv(data_path)
    print(data.head())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HyCAN Main Application")
    parser.add_argument("--data", type=str, default="data/example_data.csv", help="Path to data file")
    args = parser.parse_args()
    main(args.data)

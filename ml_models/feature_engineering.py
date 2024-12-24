
"""
Feature Engineering Module for Hydrogen Energy Research
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class FeatureEngineering:
    """
    Feature Engineering Class
    Provides methods to preprocess and scale data.
    """
    def __init__(self):
        self.scaler = StandardScaler()

    def scale_features(self, data):
        """
        Scales features using StandardScaler.
        :param data: DataFrame
        :return: DataFrame with scaled features
        """
        return pd.DataFrame(self.scaler.fit_transform(data), columns=data.columns)

    def add_interactions(self, data):
        """
        Adds interaction terms for each feature.
        :param data: DataFrame
        :return: DataFrame with interaction terms
        """
        interaction_data = pd.DataFrame()
        for col1 in data.columns:
            for col2 in data.columns:
                if col1 != col2:
                    interaction_data[f"{col1}*{col2}"] = data[col1] * data[col2]
        return pd.concat([data, interaction_data], axis=1)

import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    return predictions

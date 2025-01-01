def test_sample():
    assert 1 + 1 == 2

import pandas as pd
from HyCAN-main.models.model_inference import load_model, predict

def test_load_model_valid():
    model = load_model("src/models/pretrained_model.pkl")
    assert model is not None

def test_load_model_invalid():
    model = load_model("nonexistent_model.pkl")
    assert model is None

def test_predict_valid_model():
    model = load_model("src/models/pretrained_model.pkl")
    data = pd.DataFrame({"feature1": [1, 2], "feature2": [3, 4]})
    predictions = predict(model, data)
    assert predictions is not None

def test_predict_invalid_model():
    model = None
    data = pd.DataFrame({"feature1": [1, 2], "feature2": [3, 4]})
    predictions = predict(model, data)
    assert predictions is None

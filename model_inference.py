# File: src/models/model_inference.py

import joblib
import pandas as pd

def load_model(model_path: str):
    """Loads a pre-trained model from the given path."""
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def predict(model, input_data: pd.DataFrame):
    """Generates predictions using the loaded model."""
    try:
        predictions = model.predict(input_data)
        return predictions
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    model = load_model("src/models/pretrained_model.pkl")
    data = pd.read_csv("data/example_data.csv")
    if model and not data.empty:
        predictions = predict(model, data)
        print("Predictions:", predictions)

import json

def load_model_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)
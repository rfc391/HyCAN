import pytest
from src.main import load_data

def test_load_data_valid_file():
    result = load_data("data/example_data.csv")
    assert result["success"] is True
    assert "data" in result

def test_load_data_invalid_file():
    result = load_data("nonexistent_file.csv")
    assert result["success"] is False
    assert "error" in result

def test_preprocess_data_valid_data():
    valid_data = {"success": True, "data": {"column_name": [1, 2, 3, 4, 5]}}
    result = preprocess_data(valid_data)
    assert result["success"] is True
    assert "data" in result
    assert "normalized_column" in result["data"]

def test_preprocess_data_invalid_data():
    invalid_data = {"success": False, "error": "Some error"}
    result = preprocess_data(invalid_data)
    assert result["success"] is False
    assert "error" in result

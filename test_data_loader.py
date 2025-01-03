import pytest
from HyCAN-main.data.data_loader import validate_dataset

def test_validate_dataset_valid():
    data = [{'input': [1, 2, 3], 'output': 1}]
    assert validate_dataset(data)

def test_validate_dataset_invalid():
    data = "Invalid data format"
    assert not validate_dataset(data)

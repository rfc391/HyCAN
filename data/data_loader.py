def validate_dataset(data):
    try:
        if not isinstance(data, list):
            raise ValueError("Dataset must be a list of samples.")
        return True
    except Exception as e:
        print(f"Validation failed: {e}")
        return False
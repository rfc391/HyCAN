
from typing import List, Dict, Any
import argparse
import os

def load_data(file_path: str) -> Dict[str, Any]:
    """Loads data from a given file path."""
    print(f"DEBUG: Entering load_data with file_path={file_path}")
    try:
        import pandas as pd
        if not os.path.exists(file_path):
            print(f"DEBUG: File {file_path} does not exist.")
            raise FileNotFoundError(f"File {file_path} does not exist.")
        print(f"DEBUG: File {file_path} exists. Proceeding to load with pandas.read_csv.")
        data = pd.read_csv(file_path)
        print(f"DEBUG: Successfully loaded data. Returning success.")
        return {"success": True, "data": data}
    except FileNotFoundError as fnfe:
        print(f"DEBUG: Caught FileNotFoundError: {str(fnfe)}")
        return {"success": False, "error": "File not found."}
    except Exception as e:
        print(f"DEBUG: Caught general exception: {str(e)}")
        return {"success": False, "error": str(e)}

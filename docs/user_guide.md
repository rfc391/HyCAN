# HyCAN User Guide

This guide provides instructions on how to use HyCAN to accelerate clean hydrogen energy research.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rfc391/HyCAN.git
   cd HyCAN
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python src/visualizations/interactive_dashboard.py
   ```
   
### Dashboards
Run the interactive dashboard:
```bash
python src/visualizations/interactive_dashboard.py
```

### Data Processing
Example usage for handling missing data:
```python
from src.data_processing.preprocessing import handle_missing_data
import pandas as pd

data = pd.DataFrame({"A": [1, 2, None]})
filled_data = handle_missing_data(data)
print(filled_data)
```

### API Integration
Fetch example data from the API:
```python
from src.api.integration import fetch_example_data

example_data = fetch_example_data()
print(example_data)
```

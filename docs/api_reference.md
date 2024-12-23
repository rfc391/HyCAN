# API Reference

This section provides detailed documentation for the HyCAN API.

## Core Modules

### `main.py`
- Entry point for running HyCAN.
- Key arguments:
  - `--config`: Path to the configuration file.
  - `--output_dir`: Directory for results.

### `model.py`
Defines the HyCAN model:
- `HyCANModel`:
  - `forward(inputs)`: Processes input data and returns embeddings.

### `data.py`
Data loading utilities:
- `load_dataset(name)`: Loads the specified dataset.
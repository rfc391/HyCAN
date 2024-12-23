# HyCAN User Guide

This guide provides instructions on how to use HyCAN to accelerate clean hydrogen energy research.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rfc391/HyCAN.git
    cd HyCAN
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running Simulations

To run a simulation, use the `simulation.py` script. For example:
```bash
python simulation.py --config config.yaml

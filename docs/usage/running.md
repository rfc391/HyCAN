# Running HyCAN

After installation, use the following commands to execute HyCAN:

## Basic Execution

Run the main script with default configurations:
```bash
python main.py --config default_config.yaml
```

## Custom Configurations

You can specify custom configurations using a `.yaml` file. For example:
```bash
python main.py --config my_config.yaml
```

### Key Options
- `--config`: Path to the configuration file
- `--output_dir`: Directory for saving results

For a complete list of options, run:
```bash
python main.py --help
```
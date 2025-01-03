
"""
HyCAN Command Line Interface
Provides command-line functionality for the HyCAN project.
"""
import argparse
from typing import Optional

def setup_cli() -> argparse.ArgumentParser:
    """
    Set up command line argument parser with data file options.
    
    Returns:
        Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description='HyCAN CLI',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--data',
        help='Path to input data file',
        required=True
    )
    return parser

def main() -> None:
    """Main CLI entry point."""
    parser = setup_cli()
    args = parser.parse_args()
    print(f'HyCAN CLI Initialized with data file: {args.data}')

if __name__ == "__main__":
    main()


import argparse
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def process_data(file_path):
    logging.info(f"Processing data from {file_path}...")

def serve_dashboard():
    logging.info("Starting the dashboard...")
    try:
        subprocess.run(["python", "dashboard.py"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to start the dashboard: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HyCAN CLI")
    subparsers = parser.add_subparsers(dest="command")

    process_parser = subparsers.add_parser("process-data", help="Process data")
    process_parser.add_argument("--file", required=True, help="Path to the data file")

    serve_parser = subparsers.add_parser("serve-dashboard", help="Serve the dashboard")

    args = parser.parse_args()

    if args.command == "process-data":
        process_data(args.file)
    elif args.command == "serve-dashboard":
        serve_dashboard()
    else:
        logging.error("No command specified. Use --help for options.")

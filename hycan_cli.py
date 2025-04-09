
import argparse
from core.anomaly_detection import run_anomaly_detection
from core.dashboard import launch_dashboard

def main():
    parser = argparse.ArgumentParser(description="HyCAN CLI")
    parser.add_argument('--simulate', type=str, help="Run anomaly detection on input file")
    parser.add_argument('--dashboard', action='store_true', help="Launch web dashboard")
    args = parser.parse_args()

    if args.simulate:
        print(f"Running simulation on {args.simulate}")
        run_anomaly_detection(args.simulate)
    elif args.dashboard:
        print("Launching dashboard...")
        launch_dashboard()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()


"""
HyCAN Application
Main application entry point for the HyCAN project.

This module initializes logging and runs the dashboard interface.
"""
from data_processing.preprocessing import handle_missing_data
from visualizations.interactive_dashboard import create_dashboard
from utils.debug_utils import auto_debug
from utils.logger import setup_logging

@auto_debug
def main() -> None:
    """
    Initialize and run the HyCAN application with monitoring.
    Sets up logging and launches the interactive dashboard.
    """
    setup_logging()
    from monitoring.advanced_monitoring import monitor, Metrics
    
    start_time = time.time()
    print('HyCAN App Running...')
    
    # Record initial metrics
    monitor.record_metric('app_start', Metrics(
        response_time=time.time() - start_time,
        error_count=0,
        active_users=0,
        memory_usage=0.0
    ))
    
    create_dashboard()

if __name__ == "__main__":
    main()

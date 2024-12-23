
from prometheus_client import start_http_server, Gauge
import time

def simulate_metrics():
    example_metric = Gauge('example_metric', 'An example metric for demonstration')
    start_http_server(8000)
    print("Metrics server is running on http://localhost:8000")
    while True:
        example_metric.set(time.time() % 60)
        time.sleep(5)

if __name__ == "__main__":
    simulate_metrics()


class MockSpan:
    """
    Mock span class for testing purposes.
    """
    def __enter__(self):
        print("Starting mock span.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Ending mock span.")


class MockTracer:
    """
    Mock tracer class with span handling.
    """
    def start_as_current_span(self, name):
        print(f"Starting span with name: {name}")
        return MockSpan()


# Export a mock tracer instance
tracer = MockTracer()

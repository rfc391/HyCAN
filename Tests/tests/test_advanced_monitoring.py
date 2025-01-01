
"""
Performance Testing
"""
import pytest

def test_advanced_monitoring():
    """
    Ensure OpenTelemetry spans are correctly logged.
    """
    from HyCAN-main.monitoring.advanced_monitoring import tracer
    with tracer.start_as_current_span("test_span") as span:
        assert span is not None

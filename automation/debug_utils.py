
import sys
import logging
import time
from functools import wraps
import traceback
from typing import Any, Callable
import json

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def performance_monitor(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        logging.info(f"Function {func.__name__} took {execution_time:.2f} seconds")
        return result
    return wrapper

def auto_debug(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            logging.info(f"Executing {func.__name__}")
            logging.debug(f"Args: {json.dumps(str(args))}")
            logging.debug(f"Kwargs: {json.dumps(str(kwargs))}")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            logging.error(f"Error in {func.__name__}: {str(e)}")
            logging.error("Traceback:")
            for line in traceback.format_tb(exc_tb):
                logging.error(line.strip())
            raise
    return wrapper

def auto_debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            logging.error(f"Error in {func.__name__}: {str(e)}")
            logging.error("Traceback:")
            for line in traceback.format_tb(exc_tb):
                logging.error(line.strip())
            raise

    return wrapper

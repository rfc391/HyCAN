import logging

def setup_logging(log_file: str = "debug.log"):
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        level=logging.DEBUG
    )
    return logging.getLogger()
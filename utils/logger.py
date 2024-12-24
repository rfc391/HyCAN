import logging

def setup_logging(log_file: str = "logfile.log"):
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()
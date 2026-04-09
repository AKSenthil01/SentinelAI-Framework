import logging
from pathlib import Path


# Define the root path of the project
PROJECT_ROOT = Path(__file__).parent.parent  # Adjust .parent count based on folder depth
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)  # Automatically create the logs folder if missing

def get_custom_logger(name):
    logger = logging.getLogger(name)

    # Only add handlers if they don't already exist (prevents duplicate logs)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Define file path
        log_file = LOG_DIR / "test_run.log"

        # File Handler
        file_handler = logging.FileHandler(log_file, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
import logging
import os
from datetime import datetime

# Create a logger
logger = logging.getLogger(__name__)

# Set the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%f')}.log"


# Set the logs directory path
logs_path = os.path.join(os.getcwd(), "logs")

try:
    # Create the logs directory if it doesn't exist
    os.makedirs(logs_path, exist_ok=True)
except OSError as e:
    print(f"Error creating logs directory: {e}")
    exit(1)

# Set the log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

try:
    # Configure the logging
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
except Exception as e:
    print(f"Error configuring logging: {e}")
    exit(1)

# Test the logger
logger.info("Logging configuration set up successfully.")
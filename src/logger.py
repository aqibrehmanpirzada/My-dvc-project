import logging
from datetime import datetime
import os

logs_dir = os.path.join(os.getcwd(), "Logs")
os.makedirs(logs_dir, exist_ok=True)

log_file_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S') + ".log"
log_file_path = os.path.join(logs_dir, log_file_name)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")

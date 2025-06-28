import os
import sys
import logging

logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

log_path = "logs"
log_file_path = os.path.join(log_path, 'running_logs.log')
os.makedirs(log_path, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format=  logging_str,
    handlers= [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_file_path)
    ]   
)

logger = logging.getLogger("mlProjectLogger")




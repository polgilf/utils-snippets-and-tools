'''
import logging
import os

current_directory = os.getcwd()
file_name = 'output_log.txt'
file_path = os.path.join(current_directory, file_name)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),         # console
        logging.FileHandler(file_path)   # file
    ]
)

logging.info("Hello both!")         # console + file
logging.getLogger("console").addHandler(logging.StreamHandler())
logging.getLogger("file").addHandler(logging.FileHandler(file_path))
'''
import logging
import os

# Build a custom path for the log file
current_directory = os.getcwd()
file_name = 'output_log.txt'
file_path = os.path.join(current_directory, file_name)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # log everything INFO and above
    format="%(asctime)s [%(levelname)s] %(message)s",  # timestamp + level + message
    handlers=[
        logging.StreamHandler(),        # log to console
        logging.FileHandler(file_path)  # log to file
    ]
)

# 👇 Goes to BOTH console and file
logging.info("Hello both!")

# 👇 Goes ONLY to console:
console_logger = logging.getLogger("console_only")
console_logger.addHandler(logging.StreamHandler())  # attach only console handler
console_logger.propagate = False  # stop passing logs to root
console_logger.info("Hello console only!")

# 👇 Goes ONLY to file:
file_logger = logging.getLogger("file_only")
file_logger.addHandler(logging.FileHandler(file_path))  # attach only file handler
file_logger.propagate = False
file_logger.info("Hello file only!")


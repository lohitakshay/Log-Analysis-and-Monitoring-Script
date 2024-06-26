import logging
import time
import random

# Configure logging
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message",
    logging.WARNING: "WARNING message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR, logging.WARNING]

# Main loop to log messages
try:
    while True:
        # Randomly select a log level
        log_level = random.choice(log_levels)
        # Get the log message format for the selected log level
        log_message = formats[log_level]
        # Log the message
        logger.log(log_level, log_message)

        # Sleep for a random interval between 1 and 9 seconds
        sleep_time = random.randint(1, 9)
        time.sleep(sleep_time)
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("\nLogging interrupted. Exiting.")

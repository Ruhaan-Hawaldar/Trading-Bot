import logging
import os

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def create_logger(name, filename):
    """
    Creates and returns a logger.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler
    file_handler = logging.FileHandler(
        os.path.join(LOG_DIR, filename)
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Application logger
logger = create_logger("TradingBot", "trading.log")

# Market logger
market_logger = create_logger(
    "MarketLogger",
    "market_order.log"
)

# Limit logger
limit_logger = create_logger(
    "LimitLogger",
    "limit_order.log"
)
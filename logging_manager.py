"""
Logging utilities for ChatGPT Automation.
"""
from pathlib import Path
import logging

def setup_logger(log_level="INFO", log_dir="logs"):
    Path(log_dir).mkdir(exist_ok=True)
    logfile = Path(log_dir) / "automation.log"

    logger = logging.getLogger("chatgpt_automation")
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(logfile, encoding="utf-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

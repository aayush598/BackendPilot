# app/utils/logger.py
import logging
import os

LOG_DIR = "logs"
GEN_LOG = os.path.join(LOG_DIR, "generation.log")
ERR_LOG = os.path.join(LOG_DIR, "errors.log")

os.makedirs(LOG_DIR, exist_ok=True)

# Logger for generation steps
gen_logger = logging.getLogger("generation_logger")
gen_logger.setLevel(logging.INFO)
gen_handler = logging.FileHandler(GEN_LOG)
gen_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
gen_handler.setFormatter(gen_formatter)
gen_logger.addHandler(gen_handler)

# Logger for errors
err_logger = logging.getLogger("error_logger")
err_logger.setLevel(logging.ERROR)
err_handler = logging.FileHandler(ERR_LOG)
err_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
err_handler.setFormatter(err_formatter)
err_logger.addHandler(err_handler)

def log_info(message):
    gen_logger.info(message)

def log_error(message):
    err_logger.error(message)

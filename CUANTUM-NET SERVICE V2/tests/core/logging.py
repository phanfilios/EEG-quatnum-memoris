import logging
import os
from .config import cfg

def setup_logging(level=logging.INFO):
    os.makedirs(cfg.artifacts_dir, exist_ok=True)
    log_path = os.path.join(cfg.artifacts_dir, "system.log")
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("qmicns")a
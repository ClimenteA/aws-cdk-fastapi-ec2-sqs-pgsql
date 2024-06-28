from config import cfg
from loguru import logger as log


log.add(
    cfg.LOG_PATH,
    enqueue=True,
    level=cfg.LOG_LEVEL,
    retention=cfg.LOG_RETENTION,
)

import logging
from tglogging import TelegramLogHandler

# TelegramLogHandler is a custom handler which is inherited from an existing handler. ie, StreamHandler.

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token="5087114297:AAFnEvhz6_jjJWW_SqWbGJdbMUsQZcCjNik", 
            log_chat_id="-1001666849876", 
            update_interval="2", 
            minimum_lines="1", 
            pending_logs="200000"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("live log streaming to telegram.")

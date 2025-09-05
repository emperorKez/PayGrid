import logging
import sys
from logtail import LogtailHandler
from .config import settings


# get logger
logger = logging.getLogger("Quantifyre")
# logger = logging.getLogger(__name__)

# create formatter
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("app.log")
better_stack_handler = LogtailHandler(source_token=settings.BETTER_STACK_TOKEN)
# better_stack_handler = LogtailHandler(source_token="$SOURCE_TOKEN")


# set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# add handlers to the logger
logger.handlers = [stream_handler, file_handler, better_stack_handler]

logger.setLevel(logging.INFO)

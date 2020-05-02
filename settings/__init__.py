import os
import logging

logger = logging.getLogger(__name__)

if os.environ.get("DEV"):
    logger.info("Using hodl-rider Development settings")
    from .dev import *
else:
    logger.info("Using hodl-rider Production settings")
    from .prod import *

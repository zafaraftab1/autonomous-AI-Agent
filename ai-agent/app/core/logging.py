import logging
from app.core.logging import logger

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("agent")



logger.info(f"User query: {message}")
logger.info(f"Decision: {context.get('decision')}")
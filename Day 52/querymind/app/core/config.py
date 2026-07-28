import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("querymind")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

if not GROQ_API_KEY:
    logger.warning(
        "GROQ_API_KEY is not set. /api/generate will fail until it is configured "
        "in your .env file (local) or environment variables (Render)."
    )

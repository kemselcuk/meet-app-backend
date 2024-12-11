from fastapi import FastAPI
from .database import engine
from . import models

# Initialize the database
models.Base.metadata.create_all(bind=engine)

# This allows you to do any startup initialization
# For example, you could add initial data, run migrations, etc.
def init_db():
    """
    Initialize database with any necessary startup data
    """
    # Example: You could add default data or perform checks
    # db = next(get_db())
    # Check if any initial setup is needed
    pass

# Optional: You can add logging or other startup configurations
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Application starting...")
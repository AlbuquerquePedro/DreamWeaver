from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME')

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Log the connection URI without password for security
logger.info(f"Connecting to the database at {DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME} with user {DATABASE_USER}")

engine = create_engine(DATABASE_CONNECTION_URI, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Example usage of logging
def example_log_message():
    try:
        logger.info("Attempting to create a new session.")
        session = SessionLocal()
        logger.info("Session created successfully.")
        # Place more code here as needed
    except Exception as e:
        logger.error(f"An error occurred while creating a session: {e}")

# Call the example function to see logging in action (you can remove this call or replace it with actual function calls)
example_log_message()
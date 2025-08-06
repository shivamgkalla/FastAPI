from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed
from sqlalchemy.exc import OperationalError

load_dotenv()


# SQLALCHEMY_DATABASE_URL = "postgresql://todoapp_db_4cu2_user:S7vqXfryVM8aL9bFkArb9fhUwkDBHS0z@dpg-d2866lp5pdvs73879dag-a.singapore-postgres.render.com/todoapp_db_4cu2"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/TodoApplicationDatabase"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# ⏳ Retry logic: Try 10 times, wait 2 seconds between each
@retry(stop=stop_after_attempt(10), wait=wait_fixed(2))
def connect_to_database():
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        # Try connecting to test it
        with engine.connect() as conn:
            print("✅ Successfully connected to the database")
        return engine
    except OperationalError as e:
        print("⏳ Retrying database connection...")
        raise e


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
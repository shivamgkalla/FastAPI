from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://todoapp_db_4cu2_user:S7vqXfryVM8aL9bFkArb9fhUwkDBHS0z@dpg-d2866lp5pdvs73879dag-a.singapore-postgres.render.com/todoapp_db_4cu2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
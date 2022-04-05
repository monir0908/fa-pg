# import os
# from dotenv import load_dotenv
# load_dotenv()  # take environment variables from .env.

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_ENGINE=os.getenv("DATABASE_ENGINE")
# POSTGRES_USER=os.getenv("POSTGRES_USER")
# POSTGRES_PASS=os.getenv("POSTGRES_PASS")
# POSTGRES_HOST=os.getenv("POSTGRES_HOST")
# POSTGRES_PORT=os.getenv("POSTGRES_PORT")
# POSTGRES_DB=os.getenv("POSTGRES_DB")

# SQLALCHEMY_DATABASE_URL = DATABASE_ENGINE + "://" + POSTGRES_USER + ":" + POSTGRES_PASS+ "@" + POSTGRES_HOST + ":" + POSTGRES_PORT + "/" + POSTGRES_DB
# # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost:5432/fastapiDB"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_ENGINE=os.getenv("DATABASE_ENGINE")
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASS=os.getenv("POSTGRES_PASS")
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")
POSTGRES_DB=os.getenv("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = DATABASE_ENGINE + "://" + POSTGRES_USER + ":" +POSTGRES_PASS + "@" + POSTGRES_HOST + ":" + POSTGRES_PORT + "/" + POSTGRES_DB

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print('creating Base...')
Base = declarative_base()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = os.environ.get("DATABASE")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME
)

Engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)

SessionLocal = sessionmaker(bind=Engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ""
engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
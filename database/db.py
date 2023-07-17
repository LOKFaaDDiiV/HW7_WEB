from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/education')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

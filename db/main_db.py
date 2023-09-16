import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from models_db import *
import sqlalchemy as sq


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = sq.create_engine(DSN)

if __name__ == '__main__':
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.close()
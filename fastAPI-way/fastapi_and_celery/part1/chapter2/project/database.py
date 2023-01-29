from sqlalchemy import create_engine

from project.config import settings

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


!engine = create_engine(settings)

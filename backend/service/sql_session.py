# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os


# username = os.environ['SQL_USERNAME']
# password = os.environ['SQL_PASSWORD']
# host = os.environ['SQL_HOST']


# Base = declarative_base()

# engine = create_engine(
#     f'mysql+pymysql://{username}:{password}@{host}/tokens?charset=utf8mb4', echo=True, pool_recycle=5000, pool_pre_ping=True)


# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine, autoflush=False)
# session = Session()

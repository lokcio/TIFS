from lagom import Container, Singleton
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine(f"postgresql://{os.getenv('POSTGRESQL_USERNAME')}:{os.getenv('POSTGRESQL_PASSWORD')}@localhost:{os.getenv('POSTGRESQL_PORT')}/{os.getenv('POSTGRESQL_DATABASE')}")
session_maker = sessionmaker(bind=engine)

container = Container()
container[Connection] = engine.connect()
container[Engine] = engine
container[Session] = session_maker()
container[Base] = declarative_base()
Base.metadata.create_all(engine)


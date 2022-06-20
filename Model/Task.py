from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from container import container



class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    provider = Column(String)
    params = Column(JSON)
    interval = Column(Float)
    last_run = Column(Date)
    last_result = Column(String)
    enabled = Column(Boolean)

    def __repr__(self):
        return "<Task(name='{}',provider='{}', params='{}', interval='{}', enable='{}')>" \
            .format(self.name, self.provider, self.params, self.interval, self.enabled)
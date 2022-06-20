from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import CIDR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from container import container


class Blacklist(container[SQLAlchemy].Model):
    __tablename__ = 'blacklist'
    id = Column(Integer, primary_key=True)
    addr = Column(CIDR)
    source = Column(String)

    def __repr__(self):
        return "<Blacklist(addr='{}', source='{}')>" \
            .format(self.addr, self.source)
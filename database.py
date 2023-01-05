from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from config import PG_DSN


engine = create_engine(PG_DSN)


Base = declarative_base(bind=engine)


class AdvModel(Base):

    __tablename__ = 'app_advertisement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    description = Column(String(300), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    owner = Column(String(64), nullable=False)

    def __init__(self, owner, name, description):
        self.owner = owner
        self.name = name
        self.description = description

    def to_dict(self):
        return {"owner": self.owner,
                "name": self.name,
                "description": self.description,
                "time_created": self.time_created,
                }

    def to_dict_wd(self):
        return {"owner": self.owner,
                "name": self.name,
                "description": self.description,
                }

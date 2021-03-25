from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime

class TaskContent(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    description = Column(Text)
    status = Column(Integer, default=0)
    create_datetime = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, description=None, status=None, create_datetime=None):
        self.name = name
        self.description = description
        self.status = status
        self.create_datetime = create_datetime

    def __repr__(self):
        return '<Name %r>' % (self.name)
from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from databse import Base

class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True, index=True)
    task_title = Column(String(25))
    task_description = Column(String(50))
    is_done = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
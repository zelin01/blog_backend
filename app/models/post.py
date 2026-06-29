from sqlalchemy import Column, Integer, String, DateTime, func
from app.blogs_db.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(200),nullable = False)
    content = Column(String, nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
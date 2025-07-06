from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base


class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    text = Column(String, nullable=False)
    emotion = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    date = Column(Date, nullable=False)

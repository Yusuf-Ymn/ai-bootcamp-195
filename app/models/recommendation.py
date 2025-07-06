from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class DailySummary(Base):
    __tablename__ = "daily_summaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    diary_text = Column(String)
    emotion = Column(String)
    diary_comment = Column(String)
    ai_comment = Column(String)

from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class MotivationCard(Base):
    __tablename__ = "motivation_cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    emotion = Column(String)
    card_text = Column(String)

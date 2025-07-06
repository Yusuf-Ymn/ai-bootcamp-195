from sqlalchemy import Column, Integer, Float, String, Date
from app.core.database import Base


class DailyMetrics(Base):
    __tablename__ = "daily_metrics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    sleep_hours = Column(Float)
    water_glasses = Column(Integer)
    screen_time_hours = Column(Float)
    coffee_cups = Column(Integer)
    exercise_minutes = Column(Integer)

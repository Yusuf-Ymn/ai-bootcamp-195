from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date

from app.services.suggestions import suggest_lifestyle_tips


from app.models.metrics import DailyMetrics as MetricsModel
from app.core.database import SessionLocal

router = APIRouter()

class MetricsRequest(BaseModel):
    user_id: str
    date: date
    sleep_hours: float
    water_glasses: int
    screen_time_hours: float
    coffee_cups: int
    exercise_minutes: int

class MetricsResponse(BaseModel):
    suggestions: list[str]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/daily-metrics", response_model=MetricsResponse)
def process_daily_metrics(request: MetricsRequest, db: Session = Depends(get_db)):

    suggestions = suggest_lifestyle_tips(request.dict())


    # Veritabanına kayıt
    metrics_record = MetricsModel(
        user_id=request.user_id,
        date=request.date,
        sleep_hours=request.sleep_hours,
        water_glasses=request.water_glasses,
        screen_time_hours=request.screen_time_hours,
        coffee_cups=request.coffee_cups,
        exercise_minutes=request.exercise_minutes
    )

    db.add(metrics_record)
    db.commit()
    db.refresh(metrics_record)

    return {"suggestions": suggestions}

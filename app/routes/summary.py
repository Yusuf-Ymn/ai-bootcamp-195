from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session

from app.services.gemini import analyze_emotion_and_comment
from app.services.suggestions import suggest_lifestyle_tips
from app.services.gemini_recommendation import generate_personal_recommendation_v3
from app.models.diary import DiaryEntry as DiaryModel
from app.models.metrics import DailyMetrics as MetricsModel
from app.core.database import SessionLocal
from app.models.recommendation import DailySummary as SummaryModel

router = APIRouter()

class Metrics(BaseModel):
    user_id: str
    date: date
    sleep_hours: float
    water_glasses: int
    screen_time_hours: float
    coffee_cups: int
    exercise_minutes: int

class SummaryRequest(BaseModel):
    user_id: str
    date: date
    diary_text: str
    metrics: Metrics

class SummaryResponse(BaseModel):
    user_id: str
    date: date
    original_diary: str
    emotion: str
    diary_comment: str
    metrics: Metrics
    rule_based_suggestions: list[str]
    ai_comment: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/daily-summary", response_model=SummaryResponse)
def process_daily_summary(request: SummaryRequest, db: Session = Depends(get_db)):
    diary_result = analyze_emotion_and_comment(request.diary_text)
    suggestions = suggest_lifestyle_tips(request.metrics.dict())
    ai_comment = generate_personal_recommendation_v3(
        emotion=diary_result["emotion"],
        metrics=request.metrics.dict(),
        diary_text=request.diary_text
    )

    diary_record = DiaryModel(
        user_id=request.user_id,
        text=request.diary_text,
        emotion=diary_result["emotion"],
        comment=diary_result["comment"],
        date=request.date
    )
    db.add(diary_record)


    metrics_data = request.metrics
    metrics_record = MetricsModel(
        user_id=metrics_data.user_id,
        date=metrics_data.date,
        sleep_hours=metrics_data.sleep_hours,
        water_glasses=metrics_data.water_glasses,
        screen_time_hours=metrics_data.screen_time_hours,
        coffee_cups=metrics_data.coffee_cups,
        exercise_minutes=metrics_data.exercise_minutes
    )
    db.add(metrics_record)

    summary_record = SummaryModel(
        user_id=request.user_id,
        date=request.date,
        diary_text=request.diary_text,
        emotion=diary_result["emotion"],
        diary_comment=diary_result["comment"],
        ai_comment=ai_comment
    )
    db.add(summary_record)

    db.commit()

    return {
        "user_id": request.user_id,
        "date": request.date,
        "original_diary": request.diary_text,
        "emotion": diary_result["emotion"],
        "diary_comment": diary_result["comment"],
        "metrics": request.metrics,
        "rule_based_suggestions": suggestions,
        "ai_comment": ai_comment
    }

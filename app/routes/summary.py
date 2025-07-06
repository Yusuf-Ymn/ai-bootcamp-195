from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

from app.services.gemini import analyze_emotion_and_comment
from app.services.suggestions import suggest_lifestyle_tips
from app.services.gemini_recommendation import generate_personal_recommendation,generate_personal_recommendation_v2, generate_personal_recommendation_v3

router = APIRouter()

class DailySummaryInput(BaseModel):
    user_id: str
    date: date
    diary_text: str
    sleep_hours: Optional[float] = Field(default=None, ge=0, le=24)
    water_glasses: Optional[int] = Field(default=None, ge=0, le=20)
    screen_time_hours: Optional[float] = Field(default=None, ge=0, le=24)
    coffee_cups: Optional[int] = Field(default=None, ge=0, le=10)
    exercise_minutes: Optional[int] = Field(default=None, ge=0, le=300)

@router.post("/daily-summary")
def process_daily_summary(data: DailySummaryInput):
    diary_text = data.diary_text
    metrics = data.dict()
    del metrics["diary_text"]  # metni sadece duygu analizi için kullandım

    # 1. Duygu analizi
    emotion_result = analyze_emotion_and_comment(diary_text)
    emotion = emotion_result["emotion"]
    diary_comment = emotion_result["comment"]

    # 2. Ölçüm verisinden öneriler
    suggestions = suggest_lifestyle_tips(metrics)

    # 3. AI öneri
    ai_comment = generate_personal_recommendation_v3(
        emotion=emotion,
        metrics=metrics,
        diary_text=diary_text
    )

    return {
        "user_id": data.user_id,
        "date": data.date,
        "original_diary": diary_text,
        "emotion": emotion,
        "diary_comment": diary_comment,
        "metrics": metrics,
        "rule_based_suggestions": suggestions,
        "ai_comment": ai_comment
    }

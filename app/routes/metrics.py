from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from app.services.suggestions import suggest_lifestyle_tips
from app.services.gemini_recommendation import generate_personal_recommendation
from app.services.gemini import analyze_emotion_and_comment
router = APIRouter()

# Günlük ölçüm verisi şeması
class DailyMetrics(BaseModel):
    user_id: str
    date: date
    sleep_hours: Optional[float] = Field(default=None, ge=0, le=24)
    water_glasses: Optional[int] = Field(default=None, ge=0, le=20)
    screen_time_hours: Optional[float] = Field(default=None, ge=0, le=24)
    coffee_cups: Optional[int] = Field(default=None, ge=0, le=10)
    exercise_minutes: Optional[int] = Field(default=None, ge=0, le=300)

# Geçici bellek içi veri deposu
metrics_storage = []

@router.post("/daily-metrics")
def save_metrics(metrics: DailyMetrics):
    data = metrics.dict()
    metrics_storage.append(data)

    suggestions = suggest_lifestyle_tips(data)
    emotion_result = analyze_emotion_and_comment("Bugünkü genel ruh halini analiz et.")  # geçici prompt
    emotion = emotion_result["emotion"]

    ai_comment = generate_personal_recommendation(emotion, suggestions)

    return {
        "message": "Veri başarıyla kaydedildi.",
        "metrics": data,
        "emotion": emotion,
        "rule_based_suggestions": suggestions,
        "ai_comment": ai_comment
    }

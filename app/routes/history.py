from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Dict
from datetime import date, timedelta

# Bu get_db fonksiyonunu merkezi bir yere taşımak en iyisidir,
# ancak şimdilik diğer rotalarla tutarlı olması için burada bırakıyoruz.
from app.core.database import SessionLocal
from app.models.recommendation import DailySummary as SummaryModel

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Yanıt modeli (Response Model)
class SummaryResponse(BaseModel):
    date: date
    emotion: str
    diary_text: str
    ai_comment: str

    class Config:
        orm_mode = True


# YENİ: Analiz yanıt modeli
class AnalysisResponse(BaseModel):
    total_entries: int
    emotion_counts: Dict[str, int]


@router.get("/summaries/{user_id}", response_model=List[SummaryResponse])
def get_user_summaries(user_id: str, db: Session = Depends(get_db)):
    """
    Belirtilen kullanıcı ID'sine ait tüm geçmiş gün özetlerini,
    en yeniden en eskiye doğru sıralanmış şekilde döndürür.
    """
    summaries = db.query(SummaryModel).filter(SummaryModel.user_id == user_id).order_by(SummaryModel.date.desc()).all()

    if not summaries:
        raise HTTPException(
            status_code=404,
            detail="Bu kullanıcı için geçmiş özet kaydı bulunamadı."
        )
    return summaries


# YENİ: Duygu Analizi Endpoint'i
@router.get("/analysis/{user_id}", response_model=AnalysisResponse)
def get_emotion_analysis(
        user_id: str,
        start_date: date = Query(..., description="Analiz başlangıç tarihi (YYYY-MM-DD)"),
        end_date: date = Query(..., description="Analiz bitiş tarihi (YYYY-MM-DD)"),
        db: Session = Depends(get_db)
):
    """
    Belirtilen kullanıcı ve tarih aralığı için duygu durumu analizi yapar.
    """
    query = db.query(SummaryModel).filter(
        SummaryModel.user_id == user_id,
        SummaryModel.date >= start_date,
        SummaryModel.date <= end_date
    )

    summaries = query.all()

    if not summaries:
        raise HTTPException(
            status_code=404,
            detail="Belirtilen tarih aralığında veri bulunamadı."
        )

    emotion_counts = {}
    for summary in summaries:
        emotion = summary.emotion
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

    return {
        "total_entries": len(summaries),
        "emotion_counts": emotion_counts
    }

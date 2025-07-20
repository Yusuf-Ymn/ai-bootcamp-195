from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from datetime import date

from app.core.database import SessionLocal
from app.models.recommendation import DailySummary as SummaryModel

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class SummaryResponse(BaseModel):
    date: date
    emotion: str
    diary_text: str
    ai_comment: str

    class Config:
        orm_mode = True


@router.get("/summaries/{user_id}", response_model=List[SummaryResponse])
def get_user_summaries(user_id: str, db: Session = Depends(get_db)):
    summaries = db.query(SummaryModel).filter(SummaryModel.user_id == user_id).order_by(SummaryModel.date.desc()).all()

    if not summaries:
        raise HTTPException(
            status_code=404,
            detail="Bu kullanıcı için geçmiş özet kaydı bulunamadı."
        )
    return summaries

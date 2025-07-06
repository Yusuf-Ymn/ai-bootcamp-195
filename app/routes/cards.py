from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from app.services.motivation_card import generate_motivation_card
from app.core.database import SessionLocal
from app.models.diary import DiaryEntry
from app.models.motivation import MotivationCard
from datetime import date

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/motivation-card")
def get_motivation_card(user_id: Optional[str] = None, db: Session = Depends(get_db)):
    emotion = None

    if user_id:
        latest_entry = (
            db.query(DiaryEntry)
            .filter(DiaryEntry.user_id == user_id)
            .order_by(DiaryEntry.date.desc())
            .first()
        )
        if latest_entry and latest_entry.emotion and latest_entry.emotion != "Bilinmiyor":
            emotion = latest_entry.emotion

    card = generate_motivation_card(emotion)


    if user_id:
        record = MotivationCard(
            user_id=user_id,
            date=date.today(),
            emotion=emotion or "Bilinmiyor",
            card_text=card
        )
        db.add(record)
        db.commit()

    return {"card": card}
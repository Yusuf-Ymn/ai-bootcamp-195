from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from app.services.motivation_card import generate_motivation_card
from app.core.database import SessionLocal
from app.models.diary import DiaryEntry

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
        print("🧠 Veritabanından çekilen en son entry:", latest_entry)

        if latest_entry and latest_entry.emotion and latest_entry.emotion != "Bilinmiyor":
            emotion = latest_entry.emotion
            print("✅ Kullanılacak emotion:", emotion)
        else:
            print("⚠️ Geçerli bir emotion bulunamadı, fallback girilecek.")

    card = generate_motivation_card(emotion)
    return {"card": card}

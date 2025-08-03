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
        try:
            latest_entry = (
                db.query(DiaryEntry)
                .filter(DiaryEntry.user_id == user_id)
                .order_by(DiaryEntry.date.desc())
                .first()
            )
            if latest_entry and latest_entry.emotion and latest_entry.emotion != "Bilinmiyor":
                emotion = latest_entry.emotion
        except Exception as e:
            print(f"Günlük girişi arama hatası: {e}")
            emotion = None

    try:
        card = generate_motivation_card(emotion)

        if user_id:
            try:
                record = MotivationCard(
                    user_id=user_id,
                    date=date.today(),
                    emotion=emotion or "Bilinmiyor",
                    card_text=card
                )
                db.add(record)
                db.commit()
            except Exception as e:
                print(f"Motivasyon kartı kaydetme hatası: {e}")
                # Hata olsa bile kartı döndür

        return {"card": card}
    except Exception as e:
        print(f"Motivasyon kartı oluşturma hatası: {e}")
        return {"card": "🗣️ \"Her yeni gün, yeni bir başlangıçtır.\" – Atasözü\n💬 Bugün nasıl hissedersen hisset, yarın senin için yeni umutlar getirebilir. 🌟"}
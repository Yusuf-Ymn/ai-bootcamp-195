from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date

from app.services.gemini import analyze_emotion_and_comment
from app.models.diary import DiaryEntry as DiaryModel
from app.core.database import SessionLocal

router = APIRouter()

class DiaryRequest(BaseModel):
    user_id: str
    text: str

class DiaryResponse(BaseModel):
    user_id: str
    original_text: str
    emotion: str
    comment: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/diary-entry", response_model=DiaryResponse)
def process_diary_entry(request: DiaryRequest, db: Session = Depends(get_db)):
    result = analyze_emotion_and_comment(request.text)

    # Veritabanına kayıt
    diary_record = DiaryModel(
        user_id=request.user_id,
        text=request.text,
        emotion=result["emotion"],
        comment=result["comment"],
        date=date.today()
    )
    db.add(diary_record)
    db.commit()
    db.refresh(diary_record)

    return {
        "user_id": request.user_id,
        "original_text": request.text,
        "emotion": result["emotion"],
        "comment": result["comment"]
    }

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini import analyze_emotion_and_comment

router = APIRouter()

class DiaryEntry(BaseModel):
    user_id: str
    text: str

@router.post("/diary-entry")
def analyze_diary(entry: DiaryEntry):
    """
    Günlük yazısını AI ile analiz eder, duygu + yorum döndürür.
    """
    result = analyze_emotion_and_comment(entry.text)

    return {
        "user_id": entry.user_id,
        "original_text": entry.text,
        "emotion": result["emotion"],
        "comment": result["comment"]
    }

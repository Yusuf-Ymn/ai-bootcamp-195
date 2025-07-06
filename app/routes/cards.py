from fastapi import APIRouter
from typing import Optional
from app.services.motivation_card import generate_motivation_card

router = APIRouter()

@router.get("/motivation-card")
def get_motivation_card(emotion: Optional[str] = None):
    card = generate_motivation_card(emotion)
    return {"card": card}

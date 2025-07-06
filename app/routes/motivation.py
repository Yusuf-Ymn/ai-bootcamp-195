

#Motivasyon kartı için cards.py kullanıyoruz. Bu dosya gereksiz.

# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.services.gemini_recommendation import generate_motivation_card
#
# router = APIRouter()
#
# class MotivationRequest(BaseModel):
#     user_id: str
#     emotion: str  # örnek: "Üzgün", "Mutlu", "Kaygılı"
#
# class MotivationResponse(BaseModel):
#     message: str
#
# @router.post("/motivation-card", response_model=MotivationResponse)
# def get_motivation_card(request: MotivationRequest):
#     message = generate_motivation_card(request.emotion)
#     return {"message": message}

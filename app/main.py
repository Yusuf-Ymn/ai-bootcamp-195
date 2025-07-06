from fastapi import FastAPI
from app.routes import diary
from app.routes import metrics
from app.routes import cards
from app.routes import summary

app = FastAPI()
app.include_router(diary.router)
app.include_router(metrics.router)
app.include_router(cards.router)
app.include_router(summary.router)

@app.get("/")
def home():
    return {"message": "MentalAI API çalışıyor. "}

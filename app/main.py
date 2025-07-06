from fastapi import FastAPI
from app.routes import cards
from app.routes import summary
from app.routes import motivation
from app.core.database import Base, engine
from app.routes import diary, metrics
from app.models import recommendation

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(diary.router)
app.include_router(metrics.router)
app.include_router(cards.router)
app.include_router(summary.router)
app.include_router(motivation.router)

@app.get("/")
def home():
    return {"message": "MentalAI API çalışıyor. "}

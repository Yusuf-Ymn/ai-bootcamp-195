from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import cards, summary, diary, metrics, history
from app.core.database import Base, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# --- CORS Middleware ---
# Frontend'in backend API'ına istek göndermesine izin verir.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Tüm metodlara (GET, POST, vb.) izin ver
    allow_headers=["*"], # Tüm başlıklara izin ver
)

app.include_router(diary.router)
app.include_router(metrics.router)
app.include_router(cards.router)
app.include_router(summary.router)
app.include_router(history.router)


@app.get("/")
def home():
    return {"message": "MentalAI API çalışıyor."}
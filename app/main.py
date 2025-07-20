from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routes import cards, summary, diary, metrics, history
from app.core.database import Base, engine 

app = FastAPI(
    title="MentalAI+ API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API router’ları
app.include_router(diary.router)
app.include_router(metrics.router)
app.include_router(cards.router)
app.include_router(summary.router)
app.include_router(history.router)

# Front-end statik dosyalar
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"  # ../frontend
if not FRONTEND_DIR.exists():
    raise RuntimeError(f"Frontend directory not found: {FRONTEND_DIR}")


app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend",
)

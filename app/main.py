from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.routes import cards, summary, diary, metrics, history, auth
from app.core.database import Base, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# --- CORS Middleware ---
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static dosyaları sun
frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")

app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(diary.router)
app.include_router(metrics.router)
app.include_router(cards.router)
app.include_router(summary.router)
app.include_router(history.router)

@app.get("/")
def home():
    return FileResponse(str(frontend_path / "index.html"))

@app.get("/login")
def login_page():
    return FileResponse(str(frontend_path / "login.html"))

@app.get("/signup")
def signup_page():
    return FileResponse(str(frontend_path / "signup.html"))

@app.get("/diaries")
def diaries_page():
    return FileResponse(str(frontend_path / "diaries.html"))

@app.get("/card")
def card_page():
    return FileResponse(str(frontend_path / "card.html"))

@app.get("/analysis")
def analysis_page():
    return FileResponse(str(frontend_path / "analysis.html"))

@app.get("/_nav.html")
def nav_file():
    return FileResponse(str(frontend_path / "_nav.html"))

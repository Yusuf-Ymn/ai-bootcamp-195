from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import os

# Proje kök dizinini otomatik bul
BASE_DIR = Path(__file__).resolve().parents[2]  # mentalAI_project/
DB_PATH = BASE_DIR / "data" / "mentalai.db"

# Eğer data klasörü yoksa oluştur
os.makedirs(DB_PATH.parent, exist_ok=True)

# Veritabanı bağlantı ayarları
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print("📁 Veritabanı yolu:", DB_PATH)

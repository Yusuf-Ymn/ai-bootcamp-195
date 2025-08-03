from fastapi import APIRouter, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
import re
import hashlib
import secrets

router = APIRouter()

def hash_password(password: str) -> str:
    """Şifreyi hash'ler"""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_password(password: str) -> bool:
    """Şifre koşullarını kontrol eder"""
    if len(password) < 8:
        return False, "Şifre en az 8 karakter olmalıdır"
    
    if not re.search(r"[A-Z]", password):
        return False, "Şifre en az bir büyük harf içermelidir"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Şifre en az bir özel karakter içermelidir"
    
    return True, "Şifre geçerli"

@router.post("/register")
def register(username: str = Form(...), password: str = Form(...), email: str = Form(None), db: Session = Depends(get_db)):
    """Kullanıcı kayıt işlemi"""
    try:
        # Şifre validasyonu
        is_valid, message = validate_password(password)
        if not is_valid:
            raise HTTPException(status_code=400, detail=message)
        
        # Kullanıcı adı kontrolü
        if len(username) < 3:
            raise HTTPException(status_code=400, detail="Kullanıcı adı en az 3 karakter olmalıdır")
        
        # Kullanıcı adı benzersizlik kontrolü
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Bu kullanıcı adı zaten kullanılıyor")
        
        # Email benzersizlik kontrolü (eğer email verilmişse)
        if email:
            existing_email = db.query(User).filter(User.email == email).first()
            if existing_email:
                raise HTTPException(status_code=400, detail="Bu email adresi zaten kullanılıyor")
        
        # Yeni kullanıcı oluştur
        hashed_password = hash_password(password)
        # Benzersiz string ID oluştur
        user_id = f"user_{secrets.token_hex(8)}"
        new_user = User(
            id=user_id,
            username=username,
            password=hashed_password,
            email=email
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {"message": "Kullanıcı başarıyla kayıt oldu", "user_id": new_user.id}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Kayıt sırasında hata: {str(e)}")

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    """Kullanıcı giriş işlemi"""
    try:
        # Kullanıcıyı bul
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")
        
        # Şifre kontrolü
        hashed_password = hash_password(password)
        if user.password != hashed_password:
            raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")
        
        return {
            "message": "Giriş başarılı",
            "user_id": user.id,
            "username": user.username,
            "email": user.email
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Giriş sırasında hata: {str(e)}")

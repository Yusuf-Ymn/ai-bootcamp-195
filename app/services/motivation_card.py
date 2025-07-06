import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_motivation_card(emotion: str = None) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    if emotion:
        emotion_note = f"Kullanıcının şu anda hissettiği duygu: {emotion}."
    else:
        emotion_note = "Kullanıcının ruh hali belirtilmemiş."

    prompt = f"""
{emotion_note}

Görevin:
- Kullanıcıya moral verici, kısa ama anlamlı bir motivasyon mesajı yaz.
- Mesaj pozitif, içten ve nazik olsun.
- Sadece 1–2 cümle olsun. Emoji kullanılabilir (isteğe bağlı).
- Sadece mesajı döndür. Başka açıklama veya biçimleme yapma.
"""

    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        print("Kart üretim hatası:", e)
        return "Unutma, sen elinden gelenin en iyisini yapıyorsun. 🌟"

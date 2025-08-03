import os
import random
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Çeşitli motivasyon kartı prompt şablonları
MOTIVATION_PROMPTS = [
    """
    Sen bir dijital motivasyon asistanısın. Aşağıda kullanıcının güncel ruh hali verilmiştir:

    🧠 Ruh hali: {emotion}

    Görevin:
    1. Bu duyguya uygun, moral verici **tek bir özlü söz** seç. Bu söz bir filozof, yazar, düşünür, bilim insanı veya bir Türk/evrensel atasözü olabilir.
    2. Bu sözün **kimin sözü olduğunu belirt.**
    3. Ardından bu söz üzerine içten, arkadaşça ve pozitif bir yorum yaz. (1-2 cümle)
    4. Konuşma tonun: destekleyici, motive edici, sohbet eder gibi.
    5. Sonuçta sadece aşağıdaki formatta cevap ver:

    🗣️ "..." – Söyleyen  
    💬 (yorumun burada)

    Gereksiz açıklama, markdown, ek bilgi verme. Sadece metin çıktısı ver.  
    Cümlelerin birbirine benzemesin. Kullanıcının moduna göre yaratıcı örnekler üret.
    """,
    
    """
    Motivasyon kartı oluştur:

    Kullanıcının ruh hali: {emotion}

    Talimatlar:
    - Bu duyguya uygun bir özlü söz bul
    - Sözün sahibini belirt
    - Kısa, destekleyici bir yorum ekle
    - Format:
      🗣️ "Söz" – Kimden
      💬 Yorum

    Yaratıcı ve çeşitli ol.
    """,
    
    """
    Ruh haline özel motivasyon mesajı:

    Duygu durumu: {emotion}

    Görev:
    1. Uygun bir özlü söz seç
    2. Kaynağını belirt
    3. Kişiselleştirilmiş yorum yaz

    Çıktı formatı:
    🗣️ "Söz" – Kaynak
    💬 Kişisel yorum

    Farklı ve ilham verici ol.
    """
]

def generate_motivation_card(emotion: str = None) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Emotion değerini güvenli hale getir
    emotion_text = emotion if emotion else "bilinmiyor"
    
    # Rastgele bir prompt şablonu seç
    selected_prompt = random.choice(MOTIVATION_PROMPTS)
    prompt = selected_prompt.format(emotion=emotion_text)

    try:
        response = model.generate_content([prompt])
        print("🔍 Gemini ham yanıt:", response)

        if hasattr(response, "text") and response.text:
            return response.text.strip()

        elif hasattr(response, "candidates"):
            return response.candidates[0].content.parts[0].text.strip()

        else:
            return "🗣️ \"Karanlığın en yoğun olduğu an, şafağa en yakın olandır.\" – Thomas Fuller\n💬 Zor geçen anlar, çoğu zaman güzel günlerin habercisidir. 🌅"
    except Exception as e:
        print("Kart üretim hatası:", e)
        return "🗣️ \"Her yeni gün, yeni bir başlangıçtır.\" – Atasözü\n💬 Bugün nasıl hissedersen hisset, yarın senin için yeni umutlar getirebilir. 🌟"

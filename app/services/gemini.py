import os
import json
import re
import random
from dotenv import load_dotenv
import google.generativeai as genai

# .env dosyasından API anahtarını yükle
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Dinamik ve çeşitli prompt şablonları
PROMPT_TEMPLATES = [
    """
Aşağıda bir kullanıcının günlük yazısı bulunmaktadır.

GÖREVİN:
1. Metni dikkatle oku.  
2. Metindeki baskın duygu durumunu YALNIZCA aşağıdaki LISTEDEKİ tek kelimelik etiketlerden biriyle bildir:  
   - Mutlu  
   - Huzurlu  
   - Keyifli  
   - Sakin  
   - Nötr  
   - Kaygılı  
   - Üzgün  
   - Stresli  
   - Yorgun  
   - Öfkeli  
   - Endişeli  
   - Umutlu

   > Bu listenin dışında başka kelime KULLANMA.

3. Seçtiğin duyguya uygun, 2-3 cümlelik, empati kuran ve motive edici kısa bir YORUM yaz.  
   - Hitap etme ("Sen …") kullanabilirsin.  
   - Tıbbi tavsiye verme.  
   - En fazla bir emoji (isteğe bağlı).

4. YALNIZCA aşağıdaki JSON şablonunu üret:

{
  "emotion": "<LISTEDEKI_DUYGU_ETIKETI>",
  "comment": "<KISA_YORUM>"
}

5. JSON dışında hiçbir şey üretme. Kod bloğu, açıklama, markdown KULLANMA.

---

KULLANICININ YAZISI:
\"\"\"{{USER_TEXT}}\"\"\"
""",
    """
Bir kullanıcının günlük notunu analiz et.

ANALİZ GÖREVİ:
1. Metindeki ana duyguyu belirle (sadece şu listeden seç):
   Mutlu, Huzurlu, Keyifli, Sakin, Nötr, Kaygılı, Üzgün, Stresli, Yorgun, Öfkeli, Endişeli, Umutlu

2. Bu duyguya uygun, destekleyici bir mesaj yaz (2-3 cümle)

3. Sadece JSON formatında yanıt ver:
{
  "emotion": "DUYGU",
  "comment": "MESAJ"
}

KULLANICI METNİ:
\"\"\"{{USER_TEXT}}\"\"\"
""",
    """
Günlük yazısı analizi:

Duygu tespiti yap ve destekleyici yorum ekle.

Duygu seçenekleri: Mutlu, Huzurlu, Keyifli, Sakin, Nötr, Kaygılı, Üzgün, Stresli, Yorgun, Öfkeli, Endişeli, Umutlu

JSON çıktısı:
{
  "emotion": "DUYGU",
  "comment": "YORUM"
}

Metin:
\"\"\"{{USER_TEXT}}\"\"\"
""",
    """
Ruh hali analizi:

Kullanıcının günlük yazısını oku ve duygu durumunu belirle.

Duygu kategorileri: Mutlu, Huzurlu, Keyifli, Sakin, Nötr, Kaygılı, Üzgün, Stresli, Yorgun, Öfkeli, Endişeli, Umutlu

Görev:
1. Ana duyguyu seç
2. Kişiselleştirilmiş yorum yaz
3. JSON formatında döndür

{
  "emotion": "DUYGU",
  "comment": "KİŞİSEL_YORUM"
}

Günlük metni:
\"\"\"{{USER_TEXT}}\"\"\"
""",
    """
Duygu analizi ve destek mesajı:

Metni analiz et ve kullanıcının ruh halini anla.

Duygu etiketleri: Mutlu, Huzurlu, Keyifli, Sakin, Nötr, Kaygılı, Üzgün, Stresli, Yorgun, Öfkeli, Endişeli, Umutlu

Çıktı formatı:
{
  "emotion": "DUYGU",
  "comment": "DESTEKLEYİCİ_MESAJ"
}

Kullanıcı yazısı:
\"\"\"{{USER_TEXT}}\"\"\"
""",
    """
Günlük değerlendirmesi:

Yazıyı oku ve duygu durumunu değerlendir.

Seçenekler: Mutlu, Huzurlu, Keyifli, Sakin, Nötr, Kaygılı, Üzgün, Stresli, Yorgun, Öfkeli, Endişeli, Umutlu

Sonuç:
{
  "emotion": "DUYGU",
  "comment": "DEĞERLENDİRME"
}

Metin:
\"\"\"{{USER_TEXT}}\"\"\"
"""
]

def analyze_emotion_and_comment(user_text: str) -> dict:
    """
    Kullanıcının yazdığı günlük metni analiz ederek,
    baskın duyguyu ve yorum metnini JSON formatında döndürür.
    """
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Rastgele bir prompt şablonu seç
        selected_template = random.choice(PROMPT_TEMPLATES)
        prompt = selected_template.replace("{{USER_TEXT}}", user_text)

        # Gemini çağrısı
        response = model.generate_content([prompt])
        raw_text = response.text.strip()
        print("🔍 Gemini ham yanıt:\n", raw_text)

        # Markdown kod bloğu varsa temizle
        if raw_text.startswith("```"):
            raw_text = re.sub(r"^```json\s*|\s*```$", "", raw_text, flags=re.DOTALL).strip()

        gemini_data = json.loads(raw_text)
        emotion = gemini_data.get("emotion", "Bilinmiyor")
        comment = gemini_data.get("comment", "Yorum alınamadı.")

        # Daha çeşitli yanıtlar için ek varyasyonlar
        if emotion == "Bilinmiyor":
            fallback_comments = [
                "Bugünkü ruh halini anlayamadım ama umarım iyi hissediyorsundur.",
                "Yazdıklarını okudum, nasıl hissettiğini tam anlayamadım.",
                "Günlük yazını inceledim, duygu durumunu belirlemekte zorlandım.",
                "Metnini analiz ettim ama duygu durumunu net olarak çıkaramadım."
            ]
            comment = random.choice(fallback_comments)

    except Exception as e:
        print("❌ JSON çözümleme hatası:", e)
        fallback_emotions = ["Nötr", "Sakin", "Bilinmiyor"]
        fallback_comments = [
            "Bugünkü ruh halini anlayamadım ama umarım iyi hissediyorsundur.",
            "Yazdıklarını okudum, nasıl hissettiğini tam anlayamadım.",
            "Günlük yazını inceledim, duygu durumunu belirlemekte zorlandım."
        ]
        emotion = random.choice(fallback_emotions)
        comment = random.choice(fallback_comments)

    return {
        "emotion": emotion,
        "comment": comment
    }

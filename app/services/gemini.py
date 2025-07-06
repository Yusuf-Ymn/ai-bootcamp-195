import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT_TEMPLATE = """
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
   - Hitap etme (“Sen …”) kullanabilirsin.  
   - Tıbbi tavsiye verme.  
   - En fazla bir emoji (isteğe bağlı).

4. YALNIZCA aşağıdaki JSON şablonunu üret:  

{{
  "emotion": "<LISTEDEKI_DUYGU_ETIKETI>",
  "comment": "<KISA_YORUM>"
}}

5. JSON dışında hiçbir ek metin, açıklama, markdown bloğu veya kod etiketi KULLANMA.

---

KULLANICININ YAZISI  
\"\"\"{{USER_TEXT}}\"\"\"
"""

def analyze_emotion_and_comment(user_text: str) -> dict:
    """
    Günlük yazısını alır, Gemini-1.5-flash modeline gönderir,
    tek kelimelik duygu etiketi + yorum içeren JSON döndürür.
    """
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        prompt = PROMPT_TEMPLATE.replace("{{USER_TEXT}}", user_text)

        response = model.generate_content([prompt])
        raw_text = response.text.strip()
        print("🔍 Gemini ham yanıt:\n", raw_text)

        # Yanıtta ```json blokları varsa temizleme
        if raw_text.startswith("```"):
            raw_text = re.sub(r"^```json\s*|\s*```$", "", raw_text, flags=re.DOTALL).strip()

        gemini_data = json.loads(raw_text)
        emotion = gemini_data.get("emotion", "Bilinmiyor")
        comment = gemini_data.get("comment", "Yorum alınamadı.")
    except Exception as e:
        print("❌ JSON çözümleme hatası:", e)
        emotion = "Bilinmiyor"
        comment = "Bugünkü ruh halini anlayamadım ama umarım iyi hissediyorsundur."

    return {"emotion": emotion, "comment": comment}

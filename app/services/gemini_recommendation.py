import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_personal_recommendation(emotion: str, suggestions: list) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = f"""
Kullanıcının genel ruh hali: {emotion}

Günlük alışkanlıklarına dair öneriler:
{chr(10).join(f"- {s}" for s in suggestions)}

Bu bilgiler doğrultusunda kullanıcıya yönelik kısa, moral verici ve motive edici bir öneri yaz.
Cümleler samimi olsun, tıbbi tavsiye verme.
Emoji kullanabilirsin, maksimum 3-4 cümle.

Sadece öneriyi ver, başka açıklama yazma.
"""

    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        print("Gemini öneri üretim hatası:", e)
        return "Bugün kendine biraz zaman ayırmayı unutma 💙"


def generate_personal_recommendation_v2(emotion: str, metrics: dict) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = f"""
Aşağıda bir kullanıcının gününe dair bilgiler yer almakta:

🧠 Ruh hali: {emotion}
🛌 Uyku süresi: {metrics.get("sleep_hours", "bilinmiyor")} saat  
💧 Su tüketimi: {metrics.get("water_glasses", "bilinmiyor")} bardak  
📱 Ekran süresi: {metrics.get("screen_time_hours", "bilinmiyor")} saat  
☕ Kahve: {metrics.get("coffee_cups", "bilinmiyor")} kupa  
🏃 Egzersiz: {metrics.get("exercise_minutes", "bilinmiyor")} dakika  

Görevin:
- Bu bilgiler doğrultusunda kullanıcıya, sayıları kullanarak moral verici bir öneri yaz.
- Lütfen her ölçümle ilgili kısa bir yorum yap (en az 2 tanesine mutlaka).
- Samimi bir üslup kullan, tıbbi tavsiye verme ama eğitici–yumuşak dille uyarabilirsin.
- Yorumun sonunda bir emoji kullanabilirsin.

Sadece öneriyi döndür, başka açıklama yazma.
"""

    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        print("Gemini kişisel öneri hatası:", e)
        return "Bugün kendinle ilgilenmeyi unutma. Küçük şeyler büyük fark yaratır 🌱"


def generate_personal_recommendation_v3(
        emotion: str,
        metrics: dict,
        diary_text: str
    ) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = f"""
    Aşağıda bir kullanıcının gününe dair TAM bilgiler var.  
    Önce metni oku, sonra ölçümlere bak ve ikisine birlikte değinen,
    arkadaşça, motive edici 3-4 cümlelik tek bir öneri yaz.

    🔸 Yazarken kendini kullanıcının yakın bir dostu gibi düşün; “Samimi bir arkadaş tonda” konuş.

───────── GÜNLÜK METNİ ─────────
{diary_text}
───────── ÖLÇÜMLER ─────────
• Uyku: {metrics.get("sleep_hours", "bilinmiyor")} saat  
• Su: {metrics.get("water_glasses", "bilinmiyor")} bardak  
• Ekran süresi: {metrics.get("screen_time_hours", "bilinmiyor")} saat  
• Kahve: {metrics.get("coffee_cups", "bilinmiyor")} kupa  
• Egzersiz: {metrics.get("exercise_minutes", "bilinmiyor")} dk  
───────── DUYGU ETİKETİ ─────────
{emotion}
───────────────────────────────

🔹 Kurallar  
1. Günlük METNİNDEN 1 cümleyle bahset (kısaca “Toplantı yoğun geçmiş” gibi).  
2. Ölçüm verilerinden EN AZ İKİ tanesine rakam vererek değin.  
3. Nazik, arkadaşça, motive edici tonda konuş.  
4. Tıbbi teşhis verme; “denemek isteyebilirsin”, “faydalı olabilir” gibi yumuşak ifadeler kullan.  
5. 4–5 cümleyi geçme, sonunda 1 emoji kullanabilirsin.  
🔹 Ek Dost Tonu Kuralları
6. Samimi bir arkadaşmışsın gibi “ben olsam”, “belki sana iyi gelir” kalıpları kullanabilirsin.
7. Günlük hayattan ufak örnekler ver:
   • “Ben de geçen hafta benzerini yaşadım, 10 dakikalık yürüyüş iyi gelmişti.”
   • “Akşam yemeğinde renkli sebzeler eklemek bazen moral toparlıyor.”
8. Gereksiz resmi kelimelerden kaçın, sohbet eder gibi yaz; ama tıbbi teşhis verme.
"""

    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception:
        return "Bugün yorucu geçmiş ama küçük adımlar büyük fark yaratır. Kendine iyi bak! 🌟"


##KULLANILMIYOR GIBI
def generate_motivation_card(emotion: str) -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = f"""
Kullanıcının ruh hali: {emotion}

Kullanıcının ruh hâline uygun, motive edici ve pozitif bir olumlama mesajı yaz. 
Mesaj 1-3 cümle uzunluğunda olsun. Arkadaşça, samimi ve umut verici bir ton kullan.
İçerikte emoji kullanabilirsin. Ama çok uzatma.

Örnekler:
- "Unutma, kötü hissettiğin günler geçici. Sen güçlüsün 💪"
- "Bugün zor olabilir ama sen bunun da üstesinden gelebilirsin 🌈"
- "Her yeni gün yeni bir başlangıç. Hadi başla! ☀️"

Sadece mesajı üret, başka bir açıklama verme.
"""

    response = model.generate_content(prompt)
    return response.text.strip()

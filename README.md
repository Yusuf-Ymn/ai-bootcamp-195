# MentalAI+ 

*“Yapay zekâ destekli duygu günlüğü, alışkanlık koçu ve motivasyon arkadaşı.”*

---

## 1 | Takım Bilgileri 

|  İsim                   |  Rol                                        |
| ----------------------- | ------------------------------------------- |
| **Yusuf Yaman**         | Product Owner · Developer                   |
| **Ahmet Taha Kartal**   | Scrum Master · Developer                    |
| **Muhammed Sefa Akyüz** | Developer                                   |
| **Dilara Dereli**       | Developer                                   |
| **Abdullah Güven**      | Developer                                   |

> **Sprint‑1 Gerçekliği **  Takımımız değişti ve çok geç toplandık; sprint bitimine yalnızca birkaç gün kala fikir kesinleşti. Kişisel yoğunluklar nedeniyle bu sprintte aktif geliştirme neredeyse tek başına *Yusuf Yaman* tarafından yürütüldü. Karar: Sprint 2 itibarıyla **günlük scrum** zorunlu, görevler herkes arasında dağıtılacak.

---

## 2 | Product Backlog

[Jira üzerindeki Product Backlog'a buradan ulaşabilirsiniz.](https://bootcamp-195.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?atlOrigin=eyJpIjoiOTFkZTJjOTcwNzhhNDlkZjgzYmM4ZGFjZmNjMzQxOWUiLCJwIjoiaiJ9)


---

## 3 | Ürün Vizyonu ve Özellikler 

### 3.1 Ürün Fikri – “Akıllı Duygu Günlüğü”

Duygularımızın, uyku / su / ekran süresi gibi **günlük mikro alışkanlıklarla** yakından ilişkili olduğunu biliyoruz. *MentalAI+* bu içgörüyü aşağıdaki adımlarla gerçeğe dönüştürür:

1. **Yaz → Gönder → Hislerini Yakala**  Kullanıcı 30–60 saniyede hislerini yazar. Gemini LLM, metni okur ve *“Üzgün / Kaygılı / Mutlu …”* gibi baskın duyguyu çıkarır.
2. **Mikro Veriler → Anında İpucu**  Uyku <6 saat mi? Kahve >3 kupa mı? Su <5 bardak mı? Sistem kural tabanlı cümlelerle “💧 Bir bardak su iç, ekran süreni kısalt” gibi minik iyileştirmeler önerir.
3. **AI Koç Yorumları**  Gemini, hem duygu hem metrikleri harmanlar, 3–4 cümlelik *arkadaş tonda* bir koç mesajı üretir.
4. **Motivasyon Kartı**  Son duyguya uygun **özlü söz + kısa yorum** kartı otomatik gelir:\
   `🗣️ "Mutluluk, paylaştıkça artar." – Albert Schweitzer`\
   `💬 Bugün sevincini başkalarıyla paylaş; duygu iki kat büyüsün! 😊`
5. **Veri Kalıcılığı**  Tüm günlükler, metrikler, özetler ve kartlar SQLite’ta saklanır; ileride grafik ve hatırlatma bildirimleri için hazırdır.

---

### 3.2 Özellik Matrisi ve Canlı Örnekler

|  Modül                                   |  Özellik                 |  Gerçek İstem                       |  AI Çıktısı                                                         |
| ---------------------------------------- | ------------------------ | ----------------------------------- | ------------------------------------------------------------------- |
| **F1 – /diary‑entry**                    | Metin duygu analizi      | “İşler çok yoğundu, başım ağrıyor.” | `emotion:"Yorgun"` + “Yoğun günler seni güçlendirir, biraz dinlen!” |
| **F2 – /daily‑metrics**                  | Kural tabanlı öneri      | 4.5 saat uyku, 9 saat ekran         | “Uyku kısa, ekran uzun ➜ erken yatmayı dene 😴”                     |
| **F3 – /daily‑summary**                  | Kombine rapor + AI yorum | (metin + metrik)                    | “Hey canım, bugün biraz yorgun hissettiğini okudum, yalnızlık da seni üzmüş anlaşılan. Bence 4 saatlik uyku ve sadece 1 bardak su, 9 saatlik ekran süresiyle birleşince böyle hissetmen çok normal! Ben olsam, yarın daha erken yatıp, bol su içmeyi ve belki kısa bir yürüyüş yapmayı deneseydim; belki sana iyi gelir. Unutma, her şey yoluna girecek! 💪”       |
| **F4 – /motivation‑card**                | Özlü söz + yorum         | Son duygu `Kaygılı`                 | 🗣️ “Korkunun ilacı eylemdir.” – Emerson   💬 Küçük adımlar at, kaygı hızla azalır. |

> **AI’nın Rolü**  Gemini 1.5‑Flash prompt’larıyla: duygu sınıflandırır, kişisel koç metni yazar, motivasyon kartındaki alıntıyı seçer ve yorumlar. Kural tabanlı öneriler (su, uyku vb.) AI’ye ek besleme verisi olur; böylece AI cümleleri “4 bardak su” gibi somut rakamlarla zenginleşir.

---

### 3.3 Hedef Kitle 

- **Z‑kuşağı öğrenciler** – Sınav stresi + ekran bağımlılığı yönetimi
- **Remote çalışanlar** – “Zoom fatigue” + su‑kahve dengesi takibi
- **Mental sağlık meraklıları** – Günlük duygu farkındalığı
- **Well‑being Start‑up’ları** – API’yi entegre edip kendi uygulamasına ek destek mesajları çekmek isteyenler

> **Etkileyici Senaryo**  Ayşe, gece 4 saat uyudu, sabah “kaygılıyım” diye not düştü. MentalAI+ hemen şu mesajı gönderdi:\
> `🗣️ “En karanlık an, şafağa en yakındır.” – Fuller`\
> `💬 4 saatlik uyku kaygını tetikleyebilir. 🚶‍♀️ 10 dk açık havada yürümek ve bu gece 7 saat hedeflemek nasıl olur?`

---

## 4 | Sprint‑1 Backlog & Velocity  (100 SP)

|  #         |  User Story / Task                          | SP         |
| ---------- | ------------------------------------------- | ---------- |
| 1          | FastAPI İskeleti                            | 5          |
| 2          | Duygu Analizi Servisi                       | 8          |
| 3          | /diary‑entry Endpoint                       | 5          |
| 4          | Metrik Öneri Servisi                        | 5          |
| 5          | /daily‑metrics Endpoint                     | 5          |
| 6          | /daily‑summary Endpoint                     | 13         |
| 7          | SQLite + SQLAlchemy                         | 8          |
| 8          | Günlük & Metrik DB Kaydı                    | 8          |
| 9          | Motivasyon Kart Servisi                     | 5          |
| 10         | /motivation‑card Endpoint + DB kaydı        | 8          |
| 11         | **Basit UI Taslağı **                       | 12         |
| 12         | Repo setup + .gitignore                     | 3          |
| **Toplam** |                                             | **100 SP** |

---

## 5 | Sprint Review 

-  Backend MVP Swagger’da yeşil. 4 ana endpoint canlı demo edildi.
-  AI - Frontend entegrasyonu yapıldı.
-  Tüm database entegrasyonları yapıldı. 
-  Gemini prompt’ları tekrarı azaltacak şekilde güncellendi.
-  Proje fikri ve yapılacaklarda karar kılındı.
-  Katılım düşüktü.

### Jüriye Not 

> *“Endpoint’leri gerçek verilerle denemekten çekinmeyin; AI yorumları rakamları referans vererek gelir.”*

---

## 6 | Sprint Retrospective

|  Gözlem                         |  Aksiyon                                |
| ------------------------------- | --------------------------------------- |
| Geç başlangıç / tek geliştirici | Roller + görev listesi Sprint 2 taşındı |
| Daily Scrum yok                 | Google Meet gündelik 15 dk zorunlu      |
| Review katılımı az              | Takvim daveti, herkese görev demosu     |
| Prompt tekrarı                  | Varyasyon checklist’i                   |

---

## 7 | Ürün Durumu – Sprint 1 

### API ve Arayüzler

**Swagger Arayüzü**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/16493ba4-2f5d-49d9-bfd0-5a26a1d7bcff" alt="Swagger arayüzü" width="600"/>
</p>

**/diary-entry Arayüzü**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/7a31bfcc-7acb-4792-be90-c6992f73d8ef" alt="/diary-entry" width="600"/>
</p>

**/diary-metrics Arayüzü**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/29813f79-baf3-4481-ab76-3d6d82b7ab57" alt="/diary-metrics" width="600"/>
</p>

**/motivation-card Arayüzü**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/b99e68f9-6cf8-404d-9d88-70f7e2ce9314" alt="/motivation-card" width="600"/>
</p>

**/daily-summary Arayüzü**  
<p align="center">
  <img src="https://github.com/user-attachments/assets/79399f22-3498-4d71-a43d-7ae7a3b64f34" alt="/daily-summary" width="600"/>
</p>

---

### Veritabanı Tabloları

<p align="center">
  <img src="https://github.com/user-attachments/assets/ec731efc-e7ab-4d10-b279-16064dea0234" alt="DB Tablo 1" width="450"/>
  <img src="https://github.com/user-attachments/assets/bd22142f-a255-4d78-bed0-c5e2f7b1c0e2" alt="DB Tablo 2" width="550"/>
</p>

---

### Jira Proje Panosu

<p align="center">
  <img src="https://github.com/user-attachments/assets/1c03595c-df39-482b-bf0f-9dcf71eba4eb" alt="Jira Pano" width="600"/>
</p>



---
*Hazırlayan : ****Yusuf Yaman**** – Product Owner

```
```

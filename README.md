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
# 📌 Sprint 2 Raporu
## 1 | Sprint Notları

Sprint 1 sonrası takım olarak ciddi bir yeniden organizasyon süreci geçirdik. Takım üyeleriyle aktif iletişim kurularak görev paylaşımı yapıldı ve günlük scruma geçildi. Frontend geliştirilmeye başlandı, taslak bir arayüz oluşturuldu. Kullanıcıdan gelen veri ve kullanıcı deneyimi geri bildirimlerine göre hem backend hem frontend tarafında çeşitli iyileştirmelere gidildi. Ayrıca projeye grafiksel analiz ve kullanıcı girişi (authentication) gibi yeni özellikler eklendi. Bu sprintte Gemini LLM aktif olarak kullanıldı ve yapay zekâ unsuru güçlendirildi.

## 2 | Daily Scrum

Yazılı günlük iletişim ise WhatsApp grubumuzda yürütüldü. Aşağıda ekran görüntüsü ile örnekler verilmiştir:

<img width="1903" height="786" alt="Image" src="https://github.com/user-attachments/assets/50ab1db4-cd75-4ac3-a044-45d2db931ebe" />

<img width="720" height="1320" alt="Image" src="https://github.com/user-attachments/assets/83f8c07f-c1dd-4012-a7f3-42d30dfc7023" />

<img width="720" height="1443" alt="Image" src="https://github.com/user-attachments/assets/e56d6986-fbdd-4e78-9bf2-42eb5c6a5abf" />



## 3 | Sprint Board (Jira Screenshot)
<img width="1541" height="809" alt="Image" src="https://github.com/user-attachments/assets/0454230c-65d6-42c2-a2ca-d6ff03bdb7e1" />

## 4 | Ürün Durumu: Ekran Görüntüleri
<img width="1600" height="768" alt="Image" src="https://github.com/user-attachments/assets/1e6a1af8-57b5-4f61-8732-c0db0ecab742" />

https://github.com/user-attachments/assets/3f149bd8-cd64-4108-9258-db6af355ae7d 
## 👥 5 | Takım ve Katkı Özeti

| İsim                   | Rol                         | Sprint 2 Katkısı                                           |
|------------------------|-----------------------------|------------------------------------------------------------|
| Yusuf Yaman           | Product Owner · Backend & AI | Kod inceleme, altyapı bakımı, raporlamalar                 |
| Ahmet Taha Kartal     | Scrum Master · Backend       | Veri analizi denemeleri, Sağlık sebebiyle sınırlı katılım  |
| Muhammed Sefa Akyüz   | Developer (Data)             | Veri analizi denemeleri — Sprint 3’e ertelendi             |
| Dilara Dereli         | Developer (Frontend)         | Arayüz prototipi (HTML + Tailwind), fetch entegrasyonu     |
| Abdullah Güven        | Developer (UI)               | Tasarım geri bildirimleri (Figma notları)                  |

> ⚠️ Gözlem: Yaz dönemi staj programları ve kişisel seyahatler nedeniyle takım üyeleri projeye sınırlı zaman ayırabildi. Scrum ritüelleri tam oturtulamadı. Sprint 3’te bu eksikliklerin giderilmesi hedeflenmektedir.

---

## 🎯 6 | Sprint 2 Review

| Hedef                        | Durum        | Açıklama                                                   |
|-----------------------------|--------------|------------------------------------------------------------|
| Web arayüzü iskeleti        | ✅ Tamamlandı | `index.html`, `history.html`, `card.html` hazırlandı        |
| API ↔︎ UI entegrasyonu       | ✅ Tamamlandı | `script.js`, `history.js`, `card.js` ile fetch bağlantısı kuruldu |
| `/summaries/{user_id}` endpoint’i | ✅ Tamamlandı | Geçmiş özet verilerine erişim sağlandı                     |
| Kullanıcı giriş altyapısı   | 🚫 Eksik      | Sprint planında olmasına rağmen henüz uygulanmadı          |
| Birim test altyapısı        | 🔄 Devam Ediyor | `pytest` şablonu hazırlandı                                |
| Docker & CI yapılandırması | ⏳ Planlandı  | Sprint 3 backlog'una alındı                                |

---

## 🛠️ 7 | Teknik Kazanımlar

- 🎨 **Tailwind CSS** ile sade, responsive arayüz tasarlandı  
- 🔐 **CORS Orta Katmanı** eklendi – frontend erişim sorunları çözüldü  
- 📄 **Yeni Endpoint**: `/summaries/{user_id}` ile kullanıcı geçmişi getirilebiliyor

---

## 🚧 8 | Sprint Retrospective

| Sorun                          | Etki                  | Alınan Aksiyon                                   |
|-------------------------------|-----------------------|--------------------------------------------------|
| Yaz dönemi staj / seyahat     | Katılım dalgalı       | Haftalık sabit toplantı saati tanımlandı         |
| İletişim gecikmeleri          | PR süresi uzadı       | GitHub Projects ve Discord düzenli kullanıldı    |
| UI kapsamının artması         | Planlama kayması      | "Fonksiyon önce, görsel sonra" prensibi benimsendi |
| UI eksikliği geri bildirimi   | Kullanıcı memnuniyeti düşük | Arayüz prototipleri Sprint 3'te genişletilecek  |

---

## 📦 9 | Sprint 2 Backlog Durumu (55 / 80 SP)

| #  | Görev                         | SP | Durum     |
|----|-------------------------------|----|-----------|
| 1  | Tailwind arayüz iskeleti      | 13 | ✅         |
| 2  | API entegrasyonu              | 8  | ✅         |
| 3  | Geçmiş sayfası kartları       | 5  | ✅         |
| 4  | Motivasyon kart animasyonu    | 5  | ✅         |
| 5  | `/summaries` endpoint’i       | 8  | ✅         |
| 6  | Birim test şablonu            | 8  | 🔄 Devam   |
| 7  | Dockerfile & CI               | 5  | ⏳ Planlandı |
| 8  | Scrum toplantıları            | 3  | ❌ Yapılamadı |
| **Toplam**                         | 80 | **55 SP**  |

---

## 📌 10 | Sonraki Sprint Odakları

1. ✅ Kullanıcı giriş altyapısının tamamlanması (`JWT` tabanlı auth)
2. 📊 Trend panosu (Plotly ile duygu / metrik grafikleri)
3. 🧪 Birim testlerin genişletilmesi (endpoint güvenliği)
4. 🐳 Dockerfile ve CI/CD kurulumu
5. 🧑‍🤝‍🧑 Scrum seremonilerinin düzenli şekilde oturtulması

---

*Hazırlayan : ****Yusuf Yaman**** & ****Ahmet Taha Kartal****
🗓️ **Tarih:** 20 Temmuz 2025

```
```

# 🏁 Sprint 3 Raporu – Final Sprint

## 1️⃣ Sprint Notları  
Bu sprintte kullanıcı girişi, kayıt işlemleri, sesli giriş ve korelasyon analizleri gibi temel özelliklere odaklanıldı.
Planlanan işlerin tamamına yakını ilerletildi ancak bazı işler in progress olarak kaldı. 
Eksik kalan kullanıcı giriş sistemi geliştirildi, sesli giriş özelliği entegre edildi. 
Grafik arayüz geliştirildi, kullanıcı deneyimi iyileştirildi. Tanıtım videosu hazırlanarak jüriye sunuma hazır hale getirildi. Tüm takım üyeleri aktif katkı sağladı.

---

## 2️⃣ Daily Scrum  
Aktif olarak Whatsapp kullanıldı.
<img width="678" height="882" alt="Image" src="https://github.com/user-attachments/assets/86c5a723-1fd0-461a-81d6-764a5971ba65" />

---

## 3️⃣ Sprint Board (Jira Screenshot)  
3 Görev "IN PROGRESS" aşamasında 17 görev ise "Done" aşamasında sprinti tamamladık.
<img width="743" height="479" alt="Image" src="https://github.com/user-attachments/assets/da635b34-2807-4477-932a-08fae9c48f88" />

---

## 4️⃣ Ürün Durumu: Ekran Görüntüleri  
<img width="853" height="794" alt="Image" src="https://github.com/user-attachments/assets/27251d35-60be-4f01-a895-5ae62502cde9" />

-
<img width="1600" height="725" alt="Image" src="https://github.com/user-attachments/assets/1d862a7e-1555-4df5-aaee-f3f77ea110e4" />

-
<img width="1592" height="795" alt="Image" src="https://github.com/user-attachments/assets/cb023cff-1985-40af-bb9f-483c8410d65e" />

-
<img width="1600" height="720" alt="Image" src="https://github.com/user-attachments/assets/7394c686-dec4-4688-a152-a6c6e6b52636" />

---

## 5️⃣ Takım ve Katkı Özeti

| İsim                  | Rol                          | Katkısı                                                              |
|-----------------------|-------------------------------|---------------------------------------------------------------------|
| Yusuf Yaman           | Product Owner · Backend & AI  | JWT auth, analiz motoru, daily scrum yönetimi, proje yönlendirme    |
| Ahmet Taha Kartal     | Scrum Master · Tester         | Sprint dokümantasyonu                                               |
| Muhammed Sefa Akyüz   | Developer (Data)              | Sesli giriş, korelasyon analizi                                     |
| Dilara Dereli         | Developer (Frontend)          | Front-end geliştirme, geçmiş veriyi getirme (dashboard)             |
| Abdullah Güven        | Developer (UI)                | Sign-up ve login arayüzleri, kullanıcı akışı                        |


---

## 6️⃣ Sprint 3 Review

| Hedef                                     | Durum         | Açıklama                                                        |
|------------------------------------------|---------------|-----------------------------------------------------------------|
| Sign-up / Login                          | 🟡 In Progress | Giriş modülü geliştirilmeye devam ediliyor                      |
| Sesli giriş                              | 🟡 In Progress | Mikrofonla kullanıcı girişi prototipi hazırlanıyor             |
| Korelasyon analizi                       | 🟡 In Progress | Duygu durumu ile hafta günleri ve su miktarı ilişkisi analiz ediliyor |
| Frontend iyileştirmeleri                 | 🟡 In Progress | UI düzenlemeleri ve dashboard üzerinde çalışmalar sürüyor       |
| Tanıtım videosu ve jüriye sunum          | ✅ Tamamlandı | Sesli anlatımlı proje tanıtım videosu hazırlandı               |


---

## 7️⃣ Teknik Kazanımlar

- 🔐 JWT tabanlı kullanıcı oturumu
- 🗣️ Sesli giriş özelliği (mikrofonla)
- 📈 Korelasyon analizi (duygu/su/gün)
- 🎨 Tailwind CSS ile responsive tasarım
- 🎥 Seslendirmeli tanıtım videosu

---

## 8️⃣ Sprint Retrospective

| Sorun                                 | Etki             | Çözüm / Aksiyon                                   |
|--------------------------------------|------------------|--------------------------------------------------|
| Zaman baskısı                        | Görev çakışması  | Takım içinde paralel görev yürütüldü             |

---

## 9️⃣ Sprint 3 Backlog Durumu

| #  | Görev                                                                 | SP | Durum         |
|----|-----------------------------------------------------------------------|----|---------------|
| 1  | SCRUM-28: Sign-up                                                     | 10 | ✅ Tamamlandı |
| 2  | SCRUM-29: Login                                                       | 8  | ✅ Tamamlandı |
| 3  | SCRUM-32: Sign-up/Login için tablo oluşturma                          | 8  | ✅ Tamamlandı |
| 4  | SCRUM-31: Sesli giriş                                                 | 10 | ✅ Tamamlandı |
| 5  | SCRUM-33: Korelasyon analizleri (hafta/su/duygu durumu)               | 12 | 🟡 In Progress |
| 6  | SCRUM-34: Frontend iyileştirmeleri                                    | 10 | 🟡 In Progress |

| 📊 **Toplam SP**: 58 | ✅ **Tamamlanan SP**: 36 | 🔄 **Tamamlanma Oranı**: %62 |


---

## 🔟 Final Notlar  

- Projede hedeflerin büyük bölümü başarıyla tamamlandı  
- Yapay zekâ destekli ve kullanıcı dostu bir uygulama geliştirildi  
- Sign-up/Login, sesli giriş, korelasyon analizleri gibi temel özellikler uygulamaya entegre edildi  
- Demo videosu jüriye sunulmaya hazır hale getirildi  
- Takım çalışması ve teknik gelişim süreci etkili şekilde yürütüldü  
- Frontend ve korelasyon analizi görevleri son rötuşlar aşamasında (*In Progress*)

---

📅 **Sprint Tarihi:** 27 Temmuz – 3 Ağustos 2025  
🧠 **Hazırlayanlar:** Yusuf Yaman · Ahmet Taha Kartal


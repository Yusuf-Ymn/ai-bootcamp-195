document.addEventListener('DOMContentLoaded', () => {

    const form = document.getElementById('daily-summary-form');
    const submitButton = document.getElementById('submit-btn');
    const loadingIndicator = document.getElementById('loading-indicator');
    const resultContainer = document.getElementById('result-container');
    const resultContent = document.getElementById('result-content');
    const errorMessage = document.getElementById('error-message');

    // Güvenli parse fonksiyonları
    const safeParseFloat = (value) => {
        const parsed = parseFloat(value);
        return isNaN(parsed) ? 0 : parsed;
    };

    const safeParseInt = (value) => {
        const parsed = parseInt(value);
        return isNaN(parsed) ? 0 : parsed;
    };

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        resultContainer.classList.add('hidden');
        errorMessage.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');
        submitButton.disabled = true;
        submitButton.textContent = 'İşleniyor...';

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Kullanıcı ID'sini localStorage'dan al
        const userId = localStorage.getItem('userId');
        if (!userId) {
            errorMessage.textContent = 'Lütfen önce giriş yapın.';
            errorMessage.classList.remove('hidden');
            loadingIndicator.classList.add('hidden');
            submitButton.disabled = false;
            submitButton.textContent = 'Günü Özetle';
            return;
        }

        const today = new Date().toISOString().split('T')[0];

        const payload = {
            user_id: userId,
            date: today,
            diary_text: data.diary_text,
            metrics: {
                user_id: userId,
                date: today,
                sleep_hours: safeParseFloat(data.sleep_hours),
                water_glasses: safeParseInt(data.water_glasses),
                screen_time_hours: safeParseFloat(data.screen_time_hours),
                coffee_cups: safeParseInt(data.coffee_cups),
                exercise_minutes: safeParseInt(data.exercise_minutes)
            }
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/daily-summary', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'API ile iletişim kurulamadı.');
            }

            const result = await response.json();

            resultContent.innerHTML = `
                <p><strong>Duygu Durumun:</strong> ${result.emotion}</p>
                <p><strong>Günlük Yorumun:</strong> ${result.diary_comment}</p>
                <div class="mt-4 pt-4 border-t">
                    <p class="font-semibold text-blue-700">Kişisel Koçundan Mesaj 🤖:</p>
                    <p class="mt-1 pl-2 border-l-4 border-blue-200">${result.ai_comment}</p>
                </div>
                <div class="mt-4 pt-4 border-t">
                    <p class="font-semibold text-green-700">Yaşam Tarzı İpuçları 💡:</p>
                    <ul class="list-disc list-inside mt-1 pl-2">
                        ${result.rule_based_suggestions.map(s => `<li>${s}</li>`).join('')}
                    </ul>
                </div>
            `;
            resultContainer.classList.remove('hidden');
        } catch (error) {
            errorMessage.textContent = `Bir hata oluştu: ${error.message}`;
            errorMessage.classList.remove('hidden');
            console.error('Hata:', error);
        } finally {
            loadingIndicator.classList.add('hidden');
            submitButton.disabled = false;
            submitButton.textContent = 'Günü Özetle';
        }
    });

    // Mikrofon fonksiyonalitesi
    const micBtn = document.getElementById('mic-btn');
    if (micBtn) {
        micBtn.addEventListener('click', function() {
            if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
                const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                const recognition = new SpeechRecognition();
                
                recognition.lang = 'tr-TR';
                recognition.continuous = false;
                recognition.interimResults = false;
                
                recognition.onstart = function() {
                    micBtn.textContent = '🔴';
                    micBtn.title = 'Konuşmayı durdur';
                };
                
                recognition.onresult = function(event) {
                    const transcript = event.results[0][0].transcript;
                    document.getElementById('diary_text').value = transcript;
                };
                
                recognition.onend = function() {
                    micBtn.textContent = '🎤';
                    micBtn.title = 'Konuşmayı başlat/durdur';
                };
                
                recognition.start();
            } else {
                alert('Tarayıcınız ses tanıma özelliğini desteklemiyor.');
            }
        });
    }
});

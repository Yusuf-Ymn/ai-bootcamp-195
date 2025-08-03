document.addEventListener('DOMContentLoaded', () => {

    const form = document.getElementById('daily-summary-form');
    const submitButton = document.getElementById('submit-button');
    const loadingIndicator = document.getElementById('loading-indicator');
    const resultContainer = document.getElementById('result-container');
    const resultContent = document.getElementById('result-content');
    const errorMessage = document.getElementById('error-message');

    // Sayfa içi akıcı kaydırma fonksiyonu
    function setupSmoothScroll(triggerId, targetId) {
        const trigger = document.getElementById(triggerId);
        const target = document.getElementById(targetId);

        if (trigger && target) {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            });
        }
    }

    // "Hemen Başla" butonları için kaydırmayı ayarla
    setupSmoothScroll('start-button', 'diary-form-section');
    setupSmoothScroll('final-start-button', 'diary-form-section');

    const safeParseFloat = (value) => {
        const num = parseFloat(value);
        return isNaN(num) ? 0.0 : num;
    };
    const safeParseInt = (value) => {
        const num = parseInt(value, 10);
        return isNaN(num) ? 0 : num;
    };

    if (form) {
        form.addEventListener('submit', async function(event) {
            event.preventDefault();

            // Kullanıcı girişi kontrolü
            const user = JSON.parse(localStorage.getItem('user') || 'null');
            if (!user) {
                showError("Günlük yazmak için önce giriş yapmalısınız. <a href='/login' class='underline'>Giriş Yap</a>");
                return;
            }

            resultContainer.classList.add('hidden');
            errorMessage.classList.add('hidden');
            loadingIndicator.innerHTML = `<p class="text-lg text-gray-600">Yapay zekâ senin için düşünüyor...</p><div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mt-2"></div>`;
            loadingIndicator.classList.remove('hidden');
            submitButton.disabled = true;
            submitButton.textContent = 'İşleniyor...';

            try {
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());
                const today = new Date().toISOString().split('T')[0];
                const userId = user.user_id || user.id; // Giriş yapan kullanıcının ID'si

                if (!userId) {
                    throw new Error("Kullanıcı bilgileri bulunamadı. Lütfen tekrar giriş yapın.");
                }

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

                const response = await fetch('http://127.0.0.1:8000/daily-summary', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    let formattedError = 'Bilinmeyen bir API hatası oluştu.';
                    if (errorData.detail && Array.isArray(errorData.detail)) {
                        formattedError = 'Lütfen aşağıdaki alanları kontrol edin:\n' + errorData.detail.map(err => {
                            const fieldName = err.loc[err.loc.length - 1];
                            return `- ${fieldName}: ${err.msg}`;
                        }).join('\n');
                    } else if (errorData.detail) {
                        formattedError = errorData.detail;
                    }
                    throw new Error(formattedError);
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
                errorMessage.style.whiteSpace = 'pre-wrap';
                errorMessage.textContent = `Bir hata oluştu:\n${error.message}`;
                errorMessage.classList.remove('hidden');
                console.error('Hata Detayı:', error);
            } finally {
                loadingIndicator.classList.add('hidden');
                submitButton.disabled = false;
                submitButton.textContent = 'Günü Özetle';
            }
        });
    }
});

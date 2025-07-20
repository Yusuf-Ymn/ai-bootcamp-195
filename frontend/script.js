const form = document.getElementById('daily-summary-form');
const submitButton = document.getElementById('submit-button');
const loadingIndicator = document.getElementById('loading-indicator');
const resultContainer = document.getElementById('result-container');
const resultContent = document.getElementById('result-content');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    resultContainer.classList.add('hidden');
    errorMessage.classList.add('hidden');
    loadingIndicator.classList.remove('hidden');
    submitButton.disabled = true;
    submitButton.textContent = 'İşleniyor...';

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    const today = new Date().toISOString().split('T')[0];

    const payload = {
        user_id: data.user_id,
        date: today,
        diary_text: data.diary_text,
        metrics: {
            user_id: data.user_id,
            date: today,
            sleep_hours: parseFloat(data.sleep_hours),
            water_glasses: parseInt(data.water_glasses),
            screen_time_hours: parseFloat(data.screen_time_hours),
            coffee_cups: parseInt(data.coffee_cups),
            exercise_minutes: parseInt(data.exercise_minutes)
        }
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/daily-summary', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
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

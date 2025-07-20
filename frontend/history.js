document.addEventListener('DOMContentLoaded', () => {
    const userIdInput = document.getElementById('history_user_id');
    const fetchButton = document.getElementById('fetch-history-button');
    const historyContainer = document.getElementById('history-container');
    const loadingIndicator = document.getElementById('history-loading');
    const errorMessage = document.getElementById('history-error');

    fetchButton.addEventListener('click', fetchHistory);
    userIdInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            fetchHistory();
        }
    });

    async function fetchHistory() {
        const userId = userIdInput.value.trim();
        if (!userId) {
            showError('Lütfen bir Kullanıcı ID girin.');
            return;
        }

        showLoading(true);
        historyContainer.innerHTML = '';

        try {
            const response = await fetch(`http://127.0.0.1:8000/summaries/${userId}`);

            if (response.status === 404) {
                showError('Bu kullanıcı için geçmiş kayıt bulunamadı.');
                return;
            }

            if (!response.ok) {
                throw new Error('Geçmiş verileri alınırken bir hata oluştu.');
            }

            const summaries = await response.json();
            displaySummaries(summaries);

        } catch (error) {
            showError(error.message);
        } finally {
            showLoading(false);
        }
    }

    function displaySummaries(summaries) {
        if (summaries.length === 0) {
            showError('Bu kullanıcı için geçmiş kayıt bulunamadı.');
            return;
        }

        summaries.forEach(summary => {
            const card = document.createElement('div');
            card.className = 'bg-white p-6 rounded-2xl shadow-lg animate-fade-in';

            const formattedDate = new Date(summary.date).toLocaleDateString('tr-TR', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });

            card.innerHTML = `
                <div class="flex justify-between items-center border-b pb-2 mb-3">
                    <h3 class="font-bold text-lg text-gray-800">${formattedDate}</h3>
                    <span class="text-sm font-semibold px-3 py-1 rounded-full ${getEmotionColor(summary.emotion)}">
                        ${summary.emotion}
                    </span>
                </div>
                <div>
                    <p class="font-semibold text-gray-600">Günlük Notun:</p>
                    <blockquote class="text-gray-700 italic border-l-4 pl-4 mt-1">
                        ${summary.diary_text}
                    </blockquote>
                </div>
                <div class="mt-4 pt-4 border-t">
                    <p class="font-semibold text-blue-700">AI Koç Yorumu:</p>
                    <p class="text-gray-800 mt-1">${summary.ai_comment}</p>
                </div>
            `;
            historyContainer.appendChild(card);
        });
    }

    function getEmotionColor(emotion) {
        const colors = {
            'Mutlu': 'bg-green-100 text-green-800',
            'Keyifli': 'bg-green-100 text-green-800',
            'Huzurlu': 'bg-blue-100 text-blue-800',
            'Sakin': 'bg-blue-100 text-blue-800',
            'Umutlu': 'bg-yellow-100 text-yellow-800',
            'Nötr': 'bg-gray-200 text-gray-800',
            'Yorgun': 'bg-indigo-100 text-indigo-800',
            'Stresli': 'bg-purple-100 text-purple-800',
            'Kaygılı': 'bg-orange-100 text-orange-800',
            'Endişeli': 'bg-orange-100 text-orange-800',
            'Üzgün': 'bg-red-100 text-red-800',
            'Öfkeli': 'bg-red-200 text-red-900',
        };
        return colors[emotion] || 'bg-gray-200 text-gray-800';
    }

    function showLoading(isLoading) {
        if (isLoading) {
            loadingIndicator.classList.remove('hidden');
            errorMessage.classList.add('hidden');
        } else {
            loadingIndicator.classList.add('hidden');
        }
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
        historyContainer.innerHTML = '';
    }
});

const style = document.createElement('style');
style.innerHTML = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .animate-fade-in {
        animation: fadeIn 0.5s ease-out forwards;
    }
`;
document.head.appendChild(style);

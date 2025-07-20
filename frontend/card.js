document.addEventListener('DOMContentLoaded', () => {
    const userIdInput = document.getElementById('card_user_id');
    const fetchButton = document.getElementById('fetch-card-button');
    const cardContainer = document.getElementById('card-container');
    const cardBack = document.getElementById('card-back');
    const loadingIndicator = document.getElementById('card-loading');
    const errorMessage = document.getElementById('card-error');

    fetchButton.addEventListener('click', fetchCard);

    async function fetchCard() {
        cardContainer.classList.remove('is-flipped');
        errorMessage.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');
        fetchButton.disabled = true;

        const userId = userIdInput.value.trim();
        let apiUrl = 'http://127.0.0.1:8000/motivation-card';
        if (userId) {
            apiUrl += `?user_id=${userId}`;
        }

        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error('Motivasyon kartı alınamadı.');
            }
            const result = await response.json();

            const formattedText = result.card.replace(/\n/g, '<br>');
            cardBack.innerHTML = `<div class="p-4">${formattedText}</div>`;

            setTimeout(() => {
                loadingIndicator.classList.add('hidden');
                cardContainer.classList.add('is-flipped');
            }, 500);

        } catch (error) {
            loadingIndicator.classList.add('hidden');
            errorMessage.textContent = error.message;
            errorMessage.classList.remove('hidden');
        } finally {
            setTimeout(() => {
                fetchButton.disabled = false;
            }, 1000);
        }
    }
});

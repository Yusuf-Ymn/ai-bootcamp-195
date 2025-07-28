document.addEventListener('DOMContentLoaded', () => {
    const userIdInput = document.getElementById('user_id');
    const periodButtons = document.querySelectorAll('.period-button');
    const customRangeButton = document.getElementById('custom-range-button');
    const startDateInput = document.getElementById('start-date');
    const endDateInput = document.getElementById('end-date');
    const chartCanvas = document.getElementById('emotionChart');
    const analysisError = document.getElementById('analysis-error');

    let emotionChart = null;

    periodButtons.forEach(button => {
        button.addEventListener('click', () => handlePeriodClick(parseInt(button.dataset.period)));
    });
    customRangeButton.addEventListener('click', handleCustomRangeClick);

    async function fetchAndDrawChart(userId, startDate, endDate) {
        showError('', true);
        if (!userId) {
            showError('Lütfen bir Kullanıcı ID girin.');
            return;
        }
        try {
            const response = await fetch(`http://127.0.0.1:8000/analysis/${userId}?start_date=${startDate}&end_date=${endDate}`);
            if (response.status === 404) throw new Error('Bu tarih aralığında veri bulunamadı.');
            if (!response.ok) throw new Error('Analiz verisi alınamadı.');

            const analysis = await response.json();
            drawDoughnutChart(analysis.emotion_counts);
        } catch (error) {
            if (emotionChart) emotionChart.destroy();
            showError(error.message);
        }
    }

    function handlePeriodClick(days) {
        const userId = userIdInput.value.trim();
        const endDate = new Date();
        const startDate = new Date();
        startDate.setDate(endDate.getDate() - (days - 1));
        fetchAndDrawChart(userId, formatDate(startDate), formatDate(endDate));
    }

    function handleCustomRangeClick() {
        const userId = userIdInput.value.trim();
        const startDate = startDateInput.value;
        const endDate = endDateInput.value;
        if (!startDate || !endDate) {
            showError('Lütfen başlangıç ve bitiş tarihlerini seçin.');
            return;
        }
        if (new Date(startDate) > new Date(endDate)) {
            showError('Başlangıç tarihi, bitiş tarihinden sonra olamaz.');
            return;
        }
        fetchAndDrawChart(userId, startDate, endDate);
    }

    function drawDoughnutChart(data) {
        if (emotionChart) {
            emotionChart.destroy();
        }
        const labels = Object.keys(data);
        const values = Object.values(data);
        const total = values.reduce((sum, value) => sum + value, 0);
        const emotionColors = { 'Mutlu': '#4ade80', 'Keyifli': '#86efac', 'Huzurlu': '#60a5fa', 'Sakin': '#93c5fd', 'Umutlu': '#facc15', 'Nötr': '#d1d5db', 'Yorgun': '#818cf8', 'Stresli': '#c084fc', 'Kaygılı': '#fb923c', 'Endişeli': '#fdba74', 'Üzgün': '#f87171', 'Öfkeli': '#ef4444', 'Bilinmiyor': '#9ca3af' };
        const backgroundColors = labels.map(label => emotionColors[label] || '#e5e7eb');

        const ctx = chartCanvas.getContext('2d');
        emotionChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Duygu Dağılımı',
                    data: values,
                    backgroundColor: backgroundColors,
                    borderColor: '#ffffff',
                    borderWidth: 3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom' },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const percentage = ((context.parsed / total) * 100).toFixed(1);
                                return `${context.label}: ${context.parsed} gün (${percentage}%)`;
                            }
                        }
                    },
                    datalabels: {
                        formatter: (value, context) => {
                            const percentage = (value / total * 100);
                            return percentage < 5 ? '' : percentage.toFixed(0) + '%';
                        },
                        color: '#fff',
                        font: { weight: 'bold', size: 14 },
                        textStrokeColor: 'black',
                        textStrokeWidth: 2
                    }
                }
            },
            plugins: [ChartDataLabels]
        });
    }

    function showError(message, hide = false) {
        analysisError.textContent = message;
        if (message && !hide) {
            analysisError.classList.remove('hidden');
        } else {
            analysisError.classList.add('hidden');
        }
    }

    function formatDate(date) {
        return date.toISOString().split('T')[0];
    }
});
